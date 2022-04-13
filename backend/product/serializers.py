from rest_framework import serializers
from .models import Product
# from django.urls import reverse
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:product-details',
    )
    edit_url = serializers.SerializerMethodField()
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'url', 'edit_url', 
                  'base_price', 'discount', 'sale_price', 'email']

    def get_edit_url(self, instance):
        request = self.context.get('request')
        return reverse('product:product-edit', 
                        args=[instance.id],
                        request=request)

    def create(self, validated_data):
        email = validated_data.pop('email')
        print(email)
        return Product.objects.create(**validated_data)



