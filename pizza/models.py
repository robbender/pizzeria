from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200, unique=True)
    toppings = models.ForeignKey("Topping", on_delete=models.DO_NOTHING, blank=True, null=True)

class Topping(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    name = models.CharField(max_length=200, unique=True)
    order_no = models.CharField(max_length=200)
    pizza = models.ForeignKey(
        Pizza, on_delete=models.DO_NOTHING, blank=True, null=True)
