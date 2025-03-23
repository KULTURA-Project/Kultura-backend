# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Cart, CartItem, Wishlist
from .serializers import CartItemSerializer, WishlistSerializer , CartSerializer
from product.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist, Product , Order ,OrderItem   , Transaction
from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=cart, product=product)

        return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)

class AddToWishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            wishlist = Wishlist.objects.get(user=request.user)
        except Wishlist.DoesNotExist:
            wishlist = Wishlist.objects.create(user=request.user)

        wishlist.products.add(product)
        return Response({"message": "Product added to wishlist"}, status=status.HTTP_200_OK)
    
    
class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart_items = CartItem.objects.filter(cart__user=request.user)
            serializer = CartItemSerializer(cart_items, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class WishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            wishlist = Wishlist.objects.get(user=request.user)
            serializer = WishlistSerializer(wishlist.products.all(), many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

class RemoveFromWishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            wishlist = Wishlist.objects.get(user=request.user)
            wishlist.products.remove(product_id)
            return Response({"message": "Product removed from wishlist"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
        
        
class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            cart_item_id = request.data.get('cart_item_id')
            CartItem.objects.get(id=cart_item_id).delete()
            return Response({"message": "Item removed from cart"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
        
class UpdateCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            cart_item_id = request.data.get('cart_item_id')
            quantity = request.data.get('quantity')
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.quantity = quantity
            cart_item.save()
            return Response({"message": "Cart item updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)                 
        
        
        
class CompleteOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            customer = Customer.objects.get(user=request.user)
            order = Order.objects.create(customer=customer, total_price=request.data.get('total_price'))
            for cart_item in CartItem.objects.filter(cart__user=request.user):
                OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
                cart_item.delete()
            Transaction.objects.create(order=order, transaction_id='MockTransactionID', payment_method='card', amount=order.total_price, status='completed')
            return Response({"message": "Order completed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
from .models import Order, OrderItem, Coupon, Transaction
from .serializers import OrderSerializer, CouponSerializer, TransactionSerializer
from django.contrib.auth import get_user_model
from product.models import Product
from rest_framework import viewsets
from rest_framework.decorators import action
from django_fsm import can_proceed        
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Coupon, Transaction
from .serializers import OrderSerializer, CouponSerializer, TransactionSerializer
from django_fsm import can_proceed
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem, Coupon, Cart
from .serializers import OrderSerializer, CartSerializer, TransactionSerializer
from .models import Transaction
import logging
logger = logging.getLogger(__name__)

class OrderListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class CreateOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logger.info(f"CreateOrderView called for user {request.user.id}")
        logger.info(f"Request data: {request.data}")

        try:
            cart = request.user.cart
            logger.info(f"Cart: {cart.id}")
        except ObjectDoesNotExist:
            logger.error("Cart not found for user")
            return Response({'error': 'Cart not found for user'}, status=status.HTTP_404_NOT_FOUND)

        if not cart.items.exists():
            logger.warning("Cart is empty.")
            return Response({'error': 'Cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)

        coupon_code = request.data.get('coupon_code')
        coupon = None

        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code, active=True)
            except Coupon.DoesNotExist:
                return Response({'error': 'Invalid coupon'}, status=status.HTTP_400_BAD_REQUEST)

        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        if coupon:
            if coupon.discount_type == 'percent':
                total_price *= (1 - coupon.discount_value / 100)
            elif coupon.discount_type == 'amount':
                total_price -= coupon.discount_value

        order = Order.objects.create(
            customer=request.user,
            total_price=total_price,
            status='pending'
        )
        logger.info(f"Order created with id: {order.id}")

        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        logger.info(f"Order items created")

        cart.items.all().delete()
        logger.info("Cart cleared")

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class OrderDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            order = Order.objects.get(id=pk, customer=request.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

class ApplyCouponView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get('code')
        try:
            coupon = Coupon.objects.get(code=code, active=True)
            return Response({
                'discount_type': coupon.discount_type,
                'discount_value': coupon.discount_value
            })
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid coupon'}, status=status.HTTP_400_BAD_REQUEST)

class CheckoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart = request.user.cart
        except ObjectDoesNotExist:
            return Response({'error': 'Cart not found for user'}, status=status.HTTP_404_NOT_FOUND)
        # Include cart details, shipping options, and coupon application in the response
        return Response({
            'cart': CartSerializer(cart).data,
            'shipping_options': [],  # Add shipping options here
            'coupon': None  # Include applied coupon if any
        })

class ProcessPaymentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('order_id')
        payment_method = request.data.get('payment_method', 'card')
        transaction_id = request.data.get('transaction_id')
        amount = request.data.get('amount')

        try:
            order = Order.objects.get(id=order_id, customer=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        if order.status != 'pending':
            return Response({'error': 'Order is not in a payable state'}, status=status.HTTP_400_BAD_REQUEST)

        # Create transaction
        transaction = Transaction.objects.create(
            order=order,
            transaction_id=transaction_id,
            payment_method=payment_method,
            amount=amount,
            status='completed'
        )

        # Update order status to shipped
        # order.ship() # Assuming you have a ship method on the order
        # order.save()

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
class ShipOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            order = Order.objects.get(id=pk, customer=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        # Add logic to ship the order
        order.status = 'shipped'
        order.save()

        return Response({'status': 'Order shipped'})


class CancelOrderView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            order = Order.objects.get(id=pk, customer=request.user)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        # Add logic to cancel the order
        order.status = 'canceled'
        order.save()

        return Response({'status': 'Order canceled'})    