from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_ecommerce_products)
]
