from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    locations = models.CharField(max_length=255)
    hours = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name='stores')
