from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST'])
def index(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        return Response(data)

    return Response({'message': 'invalid data'}, status=400)