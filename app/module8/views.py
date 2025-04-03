from django.db.models import Avg, Count, F, Max, Min, Q, Sum
from drf_spectacular.utils import extend_schema
from inventory.models import (
    Category,
    OrderProduct,
    Product,
    ProductPromotionEvent,
    User,
)
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import (
    AvgCategorySerializer,
    CategorySerializer,
    MinMaxCategorySerializer,
    ProductCountSerializer,
    UserSerializer,
)


@extend_schema(
    tags=["Module 8 - Count"],
)
class CountRecordsViewSet(viewsets.ViewSet):
    """
    Demonstrates different count aggregations in Django ORM.
    """

    def list(self, request):
        # Count total products
        total_products = Product.objects.aggregate(product_count=Count("id"))

        # Count products per category
        categories_with_product_count = Category.objects.annotate(
            product_count=Count("products")
        )

        # Count orders per user
        users_with_order_count = User.objects.annotate(order_count=Count("order"))

        # Count products with active promotions
        products_with_promotion_count = ProductPromotionEvent.objects.aggregate(
            promoted_products=Count("product", distinct=True)
        )

        # Count products with no promotions
        products_without_promotion_count = Product.objects.filter(
            productpromotionevent__isnull=True
        ).aggregate(no_promotion_products=Count("id"))

        # Count products in either Category A OR Category B
        products_or = Product.objects.filter(
            Q(category__name="Books") | Q(category__name="Category B")
        ).aggregate(product_count=Count("id"))

        # Serialize data to return response
        products_data = {
            "total_products": total_products,
            "products_per_category": CategorySerializer(
                categories_with_product_count, many=True
            ).data,
            "orders_per_user": UserSerializer(users_with_order_count, many=True).data,
            "products_with_promotion": products_with_promotion_count,
            "products_without_promotion": products_without_promotion_count,
            "products_or": ProductCountSerializer(products_or).data,
        }

        return Response(products_data)


@extend_schema(
    tags=["Module 8 - Sum"],
)
class SumAggregationViewSet(viewsets.ViewSet):
    """
    Demonstrates different sum aggregations in Django ORM for summing values.
    """

    def list(self, request):
        # Sum of product prices
        total_product_price = Product.objects.aggregate(total_price=Sum("price"))

        # Sum of product prices per order (considering quantity)
        total_order_price = OrderProduct.objects.annotate(
            total_order_price=Sum(F("quantity") * F("product__price"))
        ).values("order_id", "product_id", "quantity", "total_order_price")

        # Sum of each order
        order_total_cost = (
            OrderProduct.objects.values("order")
            .annotate(total_cost=Sum(F("quantity") * F("product__price")))
            .order_by("order")
        )

        # Serialize data to return response
        products_data = {
            "total_product_price": total_product_price,
            "total_order_price": total_order_price,
            "order_total_cost": order_total_cost,
        }

        return Response(products_data)


@extend_schema(
    tags=["Module 8 - Average"],
)
class AvgAggregationViewSet(viewsets.ViewSet):
    """
    Demonstrates different avg aggregations in Django ORM for averaging values.
    """

    def list(self, request):
        avg_price = Product.objects.aggregate(avg_price=Avg("price"))

        # Calculate the average price of products per category
        categories_with_avg_price = Category.objects.annotate(
            avg_price=Avg("products__price")
        )

        # Preparing the response data
        data = {
            "average_price_of_all_products": avg_price["avg_price"],
            "average_price_per_category": AvgCategorySerializer(
                categories_with_avg_price, many=True
            ).data,
        }

        return Response(data)


@extend_schema(
    tags=["Module 8 - Having"],
)
class FilterAggregationViewSet(viewsets.ViewSet):
    """
    Demonstrates different sum aggregations in Django ORM for summing values.
    """

    def list(self, request):
        # Sum of each order
        order_total_cost = (
            OrderProduct.objects.values("order")
            .annotate(total_cost=Sum(F("quantity") * F("product__price")))
            .order_by("order")
            .filter(total_cost__gt=5000)
        )

        # Serialize data to return response
        products_data = {
            "order_total_cost": order_total_cost,
        }

        return Response(products_data)


@extend_schema(
    tags=["Module 8 - Min Max"],
)
class MinMaxAggregationViewSet(viewsets.ViewSet):
    """
    Demonstrates min max
    """

    def list(self, request):
        # Find the minimum and maximum price of products
        price_stats = Product.objects.aggregate(
            min_price=Min("price"), max_price=Max("price")
        )

        categories_with_price_stats = Category.objects.annotate(
            min_price=Min("products__price"),
            max_price=Max("products__price"),
        ).order_by("id")

        # Serialize data to return response
        products_data = {
            "min_max_cost": price_stats,
            "categories_with_price_stats": MinMaxCategorySerializer(
                categories_with_price_stats, many=True
            ).data,
        }

        return Response(products_data)
