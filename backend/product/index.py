from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from product.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = ['title', 'content', 'user', 'public']
    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['user', 'public'],
    }
    # should_index = 'is_public'
    tags = 'get_tag_list'