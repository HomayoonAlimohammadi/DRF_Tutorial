from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

app_name = 'api'
urlpatterns = [
    path('', index, name='api_index'),
    path('auth/', obtain_auth_token),
]