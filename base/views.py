from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from rest_framework.response import Response

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get(self,request):
        product_category_objs = self.get_queryset()
        serializer = self.serializer_class(product_category_objs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ProductCategoryDetailApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
        
    def get(self,request,pk):
        try:
            object = ProductCategory.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(object)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            object = ProductCategory.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            object = ProductCategory.objects.get(id=pk)
        except:
            return Response('Data not found!')
        
        object.delete()
        return Response('Data deleted!')