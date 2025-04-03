# serializers.py
from inventory.models import (
    Category,
    OrderProduct,
    Product,
    User,
)
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(
        read_only=True
    )  # Field for counted products

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "product_count"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "slug", "description", "price", "is_active", "category"]


class UserSerializer(serializers.ModelSerializer):
    order_count = serializers.IntegerField(read_only=True)  # Field for counted orders

    class Meta:
        model = User
        fields = ["id", "username", "email", "order_count"]


class ProductCountSerializer(serializers.Serializer):
    product_count = serializers.IntegerField()


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["order", "product", "quantity"]


class AvgCategorySerializer(serializers.ModelSerializer):
    avg_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "avg_price"]


class MinMaxCategorySerializer(serializers.ModelSerializer):
    min_price = serializers.IntegerField(read_only=True)
    max_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "min_price", "max_price"]
