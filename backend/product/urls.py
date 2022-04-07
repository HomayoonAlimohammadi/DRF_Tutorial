from django.urls import include, path
from product import views

app_name = 'product'

urlpatterns = [ 
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', views.ProductDestroyAPIView.as_view()),
]