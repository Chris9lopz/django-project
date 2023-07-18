from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

class Products(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    price = models.IntegerField()

class Orders(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    delivered = models.BooleanField()

