from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

