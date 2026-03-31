from rest_framework.response import Response
from .models import Product, Order, OrderItem
from .serializer import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def product_list(request):
    # Fetch products from Db
    products = Product.objects.all() # QuerySet

    # Serialize (complex data -> json)
    serializer = ProductSerializer(products, many=True)

    # Response
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    #Fetch a single product
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)

    # serialize
    serializer = ProductSerializer(product)

    # response
    return Response(serializer.data)