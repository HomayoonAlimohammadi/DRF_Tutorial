from django.urls import include, path
from product import views

app_name = 'product'

urlpatterns = [ 
    path('', views.ProductMixinView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('<int:pk>/update/', views.ProductMixinView.as_view()),
    path('<int:pk>/destroy/', views.ProductMixinView.as_view()),
]