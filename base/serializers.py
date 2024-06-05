from rest_framework import serializers
from .models import User, Product, ProductCategory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields ='__all__'