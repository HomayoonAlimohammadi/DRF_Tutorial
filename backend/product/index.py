import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from product.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = ['title', 'content', 'user']
