from django.shortcuts import render
from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def list_ecommerce_products(request):
    # Fetch products
    products = Product.objects.all()

    # Serialize
    serializer = ProductSerializer(products, many=True)

    # return response
    return Response(serializer.data)