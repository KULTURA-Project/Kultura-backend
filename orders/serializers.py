from rest_framework import serializers
from .models import Order, OrderItem , Card, Wishlist, Coupon  , CartItem , Cart ,  Promotion
from product.serializers import ProductSerializer
from product.models import Product ,  ProductImage , Category , ProductType
from rest_framework import serializers
from .models import Order, OrderItem, Coupon, Transaction

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'image','discount_percentage' ,'link']
        
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']       
        
'''class HeroPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'image', 'link']      '''  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # Nested serializer for images
    category = CategorySerializer(read_only=True)  # Nested serializer for category
    product_type = ProductTypeSerializer(read_only=True)  # Nested serializer for product type

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'slug', 'images', 'category', 'product_type']
        
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
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)  # Include category
    product_type = ProductTypeSerializer(read_only=True)  # Include product type
    class Meta:
        model = Product
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
        