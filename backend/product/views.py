from rest_framework import generics
from product import serializers, models


class ProductDetailView(generics.RetrieveAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

