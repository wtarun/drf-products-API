from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )

# --- serializers.py ---
class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(read_only=True)  # Returns __str__ of Category
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.FloatField(min_value=0.0, max_value=1.0)
    stock = serializers.IntegerField(min_value=0)
    condition = serializers.ChoiceField(choices=Product.ConditionChoices.choices)
    image = serializers.ImageField(required=False)
    final_price = serializers.SerializerMethodField()
    in_stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'price',
            'discount',
            'final_price',
            'stock',
            'in_stock',
            'condition',
            'image',
        )

    def get_final_price(self, obj):
        return round(float(obj.price) * (1 - obj.discount), 2)

    def get_in_stock(self, obj):
        return obj.stock > 0

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

