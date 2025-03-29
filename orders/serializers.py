from rest_framework import serializers
from .models import Order, OrderItem , Card, Wishlist, Coupon  , CartItem , Cart ,  Promotion
from product.serializers import ProductSerializer
<<<<<<< HEAD
from product.models import Product ,  ProductImage , Category , ProductType
from rest_framework import serializers
from .models import Order, OrderItem, Coupon, Transaction
=======
from product.models import Product
>>>>>>> parent of fb2abac (images , login ,use dashboard and so)

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'image','discount_percentage' ,'link']
        
        
'''class HeroPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'image', 'link']      '''  
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'slug', 'images']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product']
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
class WishlistSerializer(serializers.ModelSerializer):
    # Since you're serializing products directly, use ProductSerializer
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['id', 'name', 'price', 'slug', 'images', 'category', 'product_type']
        
        
        


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_price', 'status', 'created_at', 'items']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
=======
        fields = ['id', 'name', 'price', 'slug', 'images']
>>>>>>> parent of fb2abac (images , login ,use dashboard and so)
