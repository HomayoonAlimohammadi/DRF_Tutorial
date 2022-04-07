from django.urls import include, path
from product import views

app_name = 'product'

urlpatterns = [ 
    path('', views.product_alt_view),
    path('<int:pk>/', views.product_alt_view)
]