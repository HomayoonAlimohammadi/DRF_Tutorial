from rest_framework import generics
from rest_framework.response import Response

from product.models import Product 
from product.serializers import ProductSerializer

from search import client

class SearchListView(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        results = client.perform_search(query)
        
        if not query:
            return Response('', status=400)

        return Response(results) 
