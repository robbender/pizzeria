from tkinter import E
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Pizza, Topping, Cart
from .forms import PizzaForm, ToppingForm, CartForm

# Create your views here.

def startingPage(request):
    toppings = Topping.objects.all()
    pizzas = Pizza.objects.all()
    context = {
        "toppings": toppings,
        "pizzas": pizzas,
    }
    return render(request, "pizza/index.html", context)

def pizzaDetail(request, pk):
    pizza = Pizza.objects.get(id=pk)
    toppings = Topping.objects.all()

    context = {
        "pizza": pizza,
        "toppings": toppings,
    }
    return render(request, "pizza/pizza_detail.html", context)

def toppingFormView(request):
    toppingForm = ToppingForm()

    context ={
        "toppingForm": toppingForm,
    }
    if request.method == "POST":
        toppingForm = ToppingForm(request.POST)
        if toppingForm.is_valid():
            toppingForm.save()
            messages.success(request, "Topping created successfully!")
        else: 
            messages.error(request, "An error occured creating the topping.")
        return redirect("starting-page")

    return render(request, "pizza/topping_form.html", context)


def updateToppingFormView(request, pk):
    topping = Topping.objects.get(id=pk)
    toppingForm = ToppingForm(instance=topping)
    context = {
        "toppingForm": toppingForm,
        "topping": topping,
    }

    if request.method == "POST":
        toppingForm = ToppingForm(request.POST, instance=topping)
        if toppingForm.is_valid():
            try:
            # add logic to update pizza if topping is updated
                toppingForm.save()
                messages.success(request, "Topping updated successfully!")
            except Exception as e:
                error_message = e
                messages.error(request, f"An error occured updating the topping. ERROR: {error_message}")

        return redirect("starting-page")

    return render(request, "pizza/topping_edit_form.html", context)


def deleteToppingView(request, pk):
    topping = Topping.objects.get(id=pk)

    context = {
        "topping": topping,
    }

    if request.method == "POST":
        try:
            topping.delete()
            messages.success(request, "Topping was deleted successfully!")

        except Exception as e:
            error_message = e 
            messages.error(
                request, f"An error occured updating the topping. ERROR: {error_message}")
                
        return redirect("starting-page")

    return render(request, "pizza/delete.html", context)


def pizzaFormView(request):
    pizzaForm = PizzaForm()
    toppings = Topping.objects.all()

    context = {
        "pizzaForm": pizzaForm,
        "toppings": toppings
    }
    if request.method == "POST":
        pizzaForm = PizzaForm(request.POST)
        if pizzaForm.is_valid():
            pizzaForm.save()
            messages.success(request, "Pizza created successfully!")
        else:
            messages.error(request, "An error occured creating the pizza.")
        return redirect("starting-page")

    return render(request, "pizza/pizza_form.html", context)

