from django.db import models


# Create your models here.
class Zapchast(models.Model):
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)
    image = models.ImageField(upload_to='')
    status = models.BooleanField(default="False")

    def __str__(self):
        return self.name_uz


class Maxsulot(models.Model):
    zapchast = models.ForeignKey(Zapchast, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)
    description = models.TextField()
    description_ru = models.TextField()
    price = models.CharField(max_length=250)
    brand = models.CharField(max_length=100)
    brand_image = models.TextField(null=True)
    image = models.ImageField(upload_to='images', null=True)
    status = models.TextField(default='False')

    def __str__(self):
        return self.name_uz


class Order(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)
    maxsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
