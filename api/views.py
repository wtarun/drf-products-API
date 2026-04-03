from rest_framework.response import Response
from .models import Product, Order, OrderItem
from .serializer import ProductSerializer, OrderSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def product_list(request):
    # Fetch products from Db
    products = Product.objects.all() # QuerySet

    # Serialize (complex data -> json)
    serializer = ProductSerializer(products, many=True)

    # Response
    return Response(serializer.data)

# ListAPIView - used for read-only endpoints to represent a collection of model instances.
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

# APIView a class based view
class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
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

# APIView version of product detail
class ProductDetailAPIView(APIView):
    def get(self, request, product_id):
        product_detail = get_object_or_404(Product, pk=product_id)
        serializer = ProductSerializer(product_detail)
        return Response(serializer.data)

# RetrieveAPIView - used for read-only endpoints to represent a single model instance.
class ProductDetailsListView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_id'


# @api_view(['GET'])
# def order_details(request):
#     # Fetch all orders from DB
#     orders = Order.objects.all()

#     # serialize
#     serializer = OrderSerializer(orders, many=True)

#     # send response
#     return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.prefetch_related('items__product') # this fixes the N+1 query problem
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

class UserOrdersListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.request.user)



