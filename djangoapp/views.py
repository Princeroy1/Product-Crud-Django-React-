from django.shortcuts import render
from .models import Products
from .Serializers import ProductSerializer
from rest_framework import viewsets
# Create your views here.
class Productview(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
