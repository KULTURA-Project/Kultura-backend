from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from django.utils import timezone
from django.conf import settings

from viewflow.fsm import State
from enum import Enum
from vendors.models import Gestionnaire
from customers.models import CustomUser
# Get the Custom User Model
CustomUser = get_user_model()

# Define Order States
class OrderState(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    CANCELED = "canceled"

# Coupon Model
class Coupon(models.Model):
    gestionnaire = models.ForeignKey(Gestionnaire, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(
        max_length=10,
        choices=[('percent', 'Percent'), ('amount', 'Amount')],
        default='percent'
    )
    discount_value = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    usage_limit = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.code

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gestionnaire = models.ForeignKey(Gestionnaire, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[(state.value, state.name) for state in OrderState],
        default=OrderState.PENDING.value
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.customer}'

# Order Flow (State Management)
class OrderFlow:
    status = State(OrderState, default=OrderState.PENDING)

    def __init__(self, order):
        self.order = order

    @status.setter()
    def _set_status(self, value):
        self.order.status = value
        self.order.save()

    @status.getter()
    def _get_status(self):
        return self.order.status

    @status.transition(source=OrderState.PENDING, target=OrderState.SHIPPED)
    def ship(self):
        # Additional logic for shipping
        pass

    @status.transition(source=OrderState.PENDING, target=OrderState.CANCELED)
    def cancel(self):
        # Additional logic for canceling
        pass

# Order Item Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"

# Card Model
class Card(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=255)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f"Card ending {self.card_number[-4:]} for {self.customer.email}"

# Wishlist Model
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.email}'s Wishlist"

# Promotion Model
class Promotion(models.Model):
    name = models.CharField(max_length=255, default="Default Name")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    image = models.ImageField(upload_to='promotions/', blank=True, null=True)
    end_date = models.DateField()
    is_hero = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def is_active(self):
        return self.start_date <= timezone.now().date() <= self.end_date

    def get_discounted_price(self, product):
        return product.price * (1 - (self.discount_percentage / 100))

# Transaction Model
class Transaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=20, choices=[('card', 'Card'), ('paypal', 'Paypal')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} for Order {self.order.id}"

# Helper Function for Completing Payment
def complete_payment(order, transaction_id, amount):
    Transaction.objects.create(
        order=order,
        transaction_id=transaction_id,
        payment_method='card',
        amount=amount,
        status='completed'
    )
    order_flow = OrderFlow(order)
    order_flow.ship()

# Cart Model
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(default=timezone.now)  # Temporarily use default=timezone.now

    def __str__(self):
        return f"Cart for {self.user.email}"

# Cart Item Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.id}"
