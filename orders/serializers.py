from rest_framework import serializers
from .models import Order, OrderItem, Customer, Card, Wishlist, Coupon  , CartItem , Cart ,  Promotion
from product.serializers import ProductSerializer
from product.models import Product

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

class WishlistSerializer(serializers.ModelSerializer):
    # Since you're serializing products directly, use ProductSerializer
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'slug', 'images']