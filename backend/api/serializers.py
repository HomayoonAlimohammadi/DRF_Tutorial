from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    base_price = serializers.SerializerMethodField() # This is a read_only field

    class Meta:
        model = Product
        fields = ['id', 'title', 'base_price', 'sale_price']

    def get_base_price(self, obj):
        return obj.price
    