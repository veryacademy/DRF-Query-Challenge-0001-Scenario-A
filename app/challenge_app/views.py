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
    tags=["Challenge Endpoint"],
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