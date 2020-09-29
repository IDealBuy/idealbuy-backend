from django.db import models

# Create your models here.

class Supermarket(models.Model):
    super_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.super_name


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    product_unit = models.CharField(max_length = 10)
    category = models.IntegerField()

    def __str__(self):
        return self.product_name
    

class Prices(models.Model):
    price = models.IntegerField(default=50)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    super_id = models.ForeignKey(Supermarket, on_delete=models.CASCADE)

    def __str__(self):
        return self.price



