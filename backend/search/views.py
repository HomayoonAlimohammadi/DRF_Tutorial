from rest_framework import generics
from rest_framework.response import Response

from product.models import Product 
from product.serializers import ProductSerializer

from search import client

class SearchListView(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        
        public = str(request.GET.get('public')) != '0'
        
        user = None
        if request.user.is_authenticated:
            user = request.user.username

        query = request.GET.get('q')

        tags = request.GET.get('tags') or None

        results = client.perform_search(query, tags=tags,
                                        user=user, public=public)
        
        if not query:
            return Response('', status=400)

        return Response(results) 
