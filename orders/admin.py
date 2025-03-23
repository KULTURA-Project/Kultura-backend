from django.contrib import admin
from .models import Order, OrderItem, Card, Coupon, Transaction, Wishlist, Promotion, Cart, CartItem
from customers.models import CustomUser  # Import CustomUser

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'customer__email')  # Assuming CustomUser uses email

    # def get_queryset(self, request):
    #     # Customize the queryset to fetch orders for the current user
    #     qs = super().get_queryset(request)
    #     return qs.filter(customer=request.user)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('customer', 'card_number', 'card_holder', 'expiry_date')
    search_fields = ('customer__email', 'card_number', 'card_holder')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'active', 'start_date', 'end_date')
    list_filter = ('active', 'discount_type')
    search_fields = ('code',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order', 'transaction_id', 'payment_method', 'amount', 'status', 'created_at')
    list_filter = ('payment_method', 'status', 'created_at')
    search_fields = ('order__id', 'transaction_id')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percentage', 'start_date', 'end_date', 'active')
    list_filter = ('active', 'start_date', 'end_date')
    search_fields = ('name', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__email',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__email', 'product__name')
