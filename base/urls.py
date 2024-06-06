from django.urls import path
from .views import register, group_listing,login, ProductApiView, ProductCategoryApiView, ProductCategoryDetailApiView

urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('roles/',group_listing),
    path('product/',ProductApiView.as_view({'get':'list','post':'create'}),name='product'),
    path('product/<int:pk>/',ProductApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='product-detail'),
    path('product-category/',ProductCategoryApiView.as_view(),name='product-category'),
    path('product-category/<int:pk>/',ProductCategoryDetailApiView.as_view(),name='product-category-detail')
]