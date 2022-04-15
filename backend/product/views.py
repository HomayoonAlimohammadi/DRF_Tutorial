from django.http import Http404
from rest_framework import generics, mixins, status, permissions, \
                           authentication
from product import serializers, models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import viewsets


class ProductViewSets(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_create(self, serializer):

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')  

        if not content:
            content = title

        serializer.save(content=content)


class ProductUpdateAPIView(generics.UpdateAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_destroy(self, instance):
        print(instance)
        super().perform_destroy(instance)

class ProductMixinView(generics.ListCreateAPIView,
                       generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(self, request, *args, **kwargs)
        return self.list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is not None:
            content = title

        serializer.save(content=content, user=self.request.user)

    def get_queryset(self):
        qs = models.Product.objects.all()
        user = self.request.user
        try:
            qs = qs.filter(user=user)
        except TypeError as e:
            return qs.none()
        return qs


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    method = request.method 

    if method == 'GET':

        if pk is not None:
            try:
                obj = models.Product.objects.get(pk=pk)
            except models.Product.DoesNotExist:
                return Response({'msg': 'not found'}, status=404)

            serializer = serializers.ProductSerializer(obj, many=False)

            return Response(serializer.data)

        queryset = models.Product.objects.all()
        serializer = serializers.ProductSerializer(queryset, many=True)

        return Response(serializer.data)
    
    elif method == 'POST':
        print(request.data)
        
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')  

            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'msg': 'invalid data'}, status=400)
        