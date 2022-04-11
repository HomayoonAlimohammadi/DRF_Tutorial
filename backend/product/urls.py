from django.urls import include, path
from product import views
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('', views.ProductViewSets)
# print(router.urls)

app_name = 'product'

urlpatterns = [ 
    path('', views.ProductMixinView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('<int:pk>/update/', views.ProductMixinView.as_view()),
    path('<int:pk>/destroy/', views.ProductMixinView.as_view()),
    # path('', include(router.urls))
]