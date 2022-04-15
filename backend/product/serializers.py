from rest_framework import serializers
from .models import Product
# from django.urls import reverse
from rest_framework.reverse import reverse
from product import validators


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product:product-details',
    )
    edit_url = serializers.SerializerMethodField()
    write_only_field = serializers.CharField(write_only=True)
    title = serializers.CharField(
        validators=[validators.unique_validator]
    )
    email = serializers.EmailField(source='user.email', read_only=True)
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'url', 'edit_url', 'user', 'email',
                  'base_price', 'discount', 'sale_price', 'write_only_field']

    def get_edit_url(self, instance):
        request = self.context.get('request')
        return reverse('product:product-edit', 
                        args=[instance.id],
                        request=request)

    def create(self, validated_data):
        email = validated_data.pop('write_only_field')
        print(email)
        return Product.objects.create(**validated_data)



