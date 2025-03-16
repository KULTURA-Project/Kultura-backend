from rest_framework import serializers
from .models import ProductType, Category, Product, Variant, VariantValue, ProductImage, ProductSpecification
from django.conf import settings
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'

class VariantValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantValue
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    variant_values = VariantValueSerializer(many=True, read_only=True)

    class Meta:
        model = Variant
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['image'] = f"{settings.MEDIA_URL}{instance.image}"
        return ret

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_type = ProductTypeSerializer(read_only=True)
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'history', 
            'category', 'product_type', 'specifications', 'images', 'gestionnaire'
        ]
        
class ProductPageSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_type = ProductTypeSerializer(read_only=True)
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'history', 'slug',
            'category', 'product_type', 'specifications', 'images', 'gestionnaire'
        ]        