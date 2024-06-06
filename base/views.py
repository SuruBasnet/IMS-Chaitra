from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer, UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, DjangoModelPermissions,IsAuthenticated
from django.contrib.auth.models import Group

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)

    if user == None:
        return Response('Invalid credentials!')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)

@api_view(['GET'])
@permission_classes([AllowAny])
def group_listing(request):
    objs = Group.objects.all()
    serializer = GroupSerializer(objs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response('User created!')
    else:
        return Response(serializer.errors)

class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]


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