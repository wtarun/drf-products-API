from rest_framework import serializers
from .models import Product, Order, OrderItem

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            # 'formatted_price',
            'stock',
        )

    # field-level validation
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError( "Price must be greater than 0.")
        return value

    
    def get_price(self, obj):
        return f"${obj.price}"
        

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'quantity',
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only = True)
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.items.all()
        # return sum(order_item.item_subtotal for order_item in order_items) - this is a generator type expression
        total = 0
        for order_item in order_items:
            total += order_item.item_subtotal
            return total
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'created_at',
            'status',
            'items',
            'total_price',
        )