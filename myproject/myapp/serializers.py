# myapp/serializers.py
from rest_framework import serializers
from .models import APIKey,Contact,Product

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['key', 'created_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'add_on', 'is_approved']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'category', 'subcategory', 'price', 'desc', 'pub_date', 'image']