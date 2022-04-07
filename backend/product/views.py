from rest_framework import generics
from product import serializers, models
from rest_framework.response import Response
from rest_framework.decorators import api_view


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


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    method = request.method 

    if method == 'GET':

        if pk is not None:
            obj = models.Product.objects.get(pk=pk)

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
        