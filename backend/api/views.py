from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def index(request, *args, **kwargs):

    instance = Product.objects.all().order_by('?').first()
    data = ProductSerializer(instance).data

    return Response(data)