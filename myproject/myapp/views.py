# myapp/views.py
from rest_framework import generics
from .models import APIKey,Contact,Product
from .serializers import APIKeySerializer,ContactSerializer,ProductSerializer

class APIKeyListCreateView(generics.ListCreateAPIView):
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.values()
    serializer_class = ProductSerializer