# myapp/urls.py
from django.urls import path
from .views import APIKeyListCreateView,ContactListCreateView,ProductListCreateView

urlpatterns = [
    path('apikeys/', APIKeyListCreateView.as_view(), name='apikeys'),
    path('contact/', ContactListCreateView.as_view(), name='contact'),
    path('product/', ProductListCreateView.as_view(), name='product'),
]
