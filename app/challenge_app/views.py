from drf_spectacular.utils import extend_schema
from inventory.models import Product
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

#################################
# Challenge serializer
#################################


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
        ]


#################################
# Challenge Viewset
#################################


@extend_schema(
    tags=["Challenge Endpoint"],
    responses={200: ProductSerializer(many=True)},
)
class ChallengeViewSet(ViewSet):
    """
    Retrieve all active products from the database.
    """

    def list(self, request):
        products = (
            #############
            # Write your solution.
            #############
        )

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
