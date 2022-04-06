from django.urls import include, path
from product import views

app_name = 'product'

urlpatterns = [ 
    path('<int:pk>/', views.ProductDetailView.as_view())
]