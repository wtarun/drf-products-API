from django.urls import path
from . import views

urlpatterns = [
    # path('products', views.product_list),
    path('products', views.ProductAPIView.as_view()), # class based views
    path('list/products/', views.ProductListAPIView.as_view()), # generic class-based views
    # path('products/<int:id>', views.product_detail),
    # path('products/<int:product_id>', views.ProductDetailsListView.as_view()),
    path('products/<int:product_id>', views.ProductDetailAPIView.as_view()),
    path('orders/', views.order_list),
    path('user-orders/', views.UserOrdersListView.as_view())
]
