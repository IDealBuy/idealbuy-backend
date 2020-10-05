from django.db import models

class Boss(models.Model):
    admin_name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)

    admin_photo = models.CharField(max_length=255)
    role = models.CharField(max_length=3)

    active = models.BooleanField(default = True)

    def __str__(self):
        return self.admin_name
    

class User(models.Model):
    username = models.CharField(max_length = 40)
    user_mail = models.EmailField(max_length = 100)
    user_photo = models.CharField(max_length = 255)
    role = models.CharField(max_length=3)
    user_firebase = models.CharField(max_length=255, default="ln3nj45k")

    active = models.BooleanField(default=True)
    def __str__(self):
        return self.username

class Supermarket(models.Model):
    super_name = models.CharField(max_length=40)
    super_mail = models.EmailField(max_length = 100)

    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)  
    super_photo = models.CharField(max_length = 255)
    role = models.CharField(max_length=3)

    active = models.BooleanField(default=True)
    def __str__(self):
        return self.super_name


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(default='Descripcion no disponible')
    product_unit = models.CharField(max_length = 10)
    product_photo = models.CharField(max_length=255, default='go.google.com')
    category = models.CharField(max_length = 20,blank=False)

    #active = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name
    

class Prices(models.Model):
    products_id = models.ForeignKey(Products, on_delete=models.PROTECT)
    super_id = models.ForeignKey(Supermarket, on_delete=models.PROTECT)
    price = models.IntegerField(blank=False)


    def __int__(self):
        return self.price
