from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    groups = models.ManyToManyField(Group)
    username = models.CharField(max_length=300,default='username')
    phone_no = models.IntegerField(null=True)
    address = models.CharField(max_length=300,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_no','address']

class ProductCategory(models.Model):
    name = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=300)
    floor = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    stock = models.IntegerField()
    category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    department = models.ManyToManyField(Department, null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    contact = models.IntegerField()
    address = models.CharField(max_length=300)
    email = models.EmailField()

class Purchase(models.Model):
    quantity = models.IntegerField()
    price  = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)