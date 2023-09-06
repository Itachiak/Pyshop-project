from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    cloth = models.CharField(max_length=100)
    size = models.CharField(max_length=5)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=55)
    discount = models.FloatField()


