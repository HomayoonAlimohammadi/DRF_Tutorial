from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):

    data = request.body
    params = request.GET
    print(params)
    user = request.GET['user']
    print(user)
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        data = {}

    return JsonResponse(data)