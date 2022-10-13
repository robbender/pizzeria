from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200, unique=True)
    toppings = models.ManyToManyField(
        "Topping", through="PizzaTopping", related_name="toppings")


class Topping(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class PizzaTopping(models.Model):
    toppings = models.ForeignKey(
        "Topping", on_delete=models.CASCADE, blank=True, null=True)
    pizza = models.ForeignKey(
        "Pizza", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    name = models.CharField(max_length=200, unique=True)
    order_no = models.CharField(max_length=200)
    pizza = models.ForeignKey(
        Pizza, on_delete=models.CASCADE, blank=True, null=True)
