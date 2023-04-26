from django.db import models
from django.db.models import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')


class Product(models.Model):
    name = models.CharField(max_length=255)
    seller = models.ForeignKey(Seller, CASCADE)
    delivery_day = models.IntegerField()
    delivery_fee = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ForeignKey(Photo, CASCADE)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
