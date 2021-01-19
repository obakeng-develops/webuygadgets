from django.db import models
from products.models import Product

# Create your models here.
class Seller(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    cellphone_number = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)