from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Pizza, Topping, Cart
from .forms import PizzaForm, ToppingForm, CartForm

# Create your views here.

def startingPage(request):
    toppings = Topping.objects.all()
    context = {
        "toppings": toppings,
    }
    return render(request, "pizza/index.html", context)

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