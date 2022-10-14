from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Pizza, Topping, Cart, PizzaTopping
from .forms import PizzaForm, ToppingForm, CartForm

# Create your views here.

def startingPage(request):
    toppings = Topping.objects.all()
    pizzas = Pizza.objects.all()
    # pizza_toppings = PizzaTopping.objects.all()
    context = {
        "toppings": toppings,
        "pizzas": pizzas,
        # "pizza_toppings": pizza_toppings,
    }
    return render(request, "pizza/starting_page.html", context)

def pizzaDetail(request, pk):
    pizza = Pizza.objects.get(id=pk)
    toppings = Topping.objects.all()
    # pizza_topping = PizzaTopping.objects.filter(pizza__id=pk)
    # print("pizza topping:", pizza_topping)
    context = {
        "pizza": pizza,
        "toppings": toppings,
        # "pizza_topping": pizza_topping
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
        "obj": topping,
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
        "toppings": toppings,
    }

    if request.method == "POST":
        pizzaForm = PizzaForm(request.POST)

        if pizzaForm.is_valid():
            # if this is a menu app and only one type of pizza could be saved
            # pizzaForm.save(commit=False)
            # save pizza description or name with sorted list of toppings
    
            pizzaForm.save()
            messages.success(request, "Pizza created successfully!")
        else:
            messages.error(request, "An error occured creating the pizza.")
        return redirect("starting-page")

    return render(request, "pizza/pizza_form.html", context)


def updatePizzaFormView(request, pk):
    pizza = Pizza.objects.get(id=pk)
    pizzaForm = PizzaForm(instance=pizza)
    # topping = Topping.objects.get(id=pk)

    context = {
        "pizzaForm": pizzaForm,
        # "topping": topping,
        "pizza": pizza,
    }

    if request.method == "POST":
        pizzaForm = PizzaForm(request.POST, instance=pizza)
        if pizzaForm.is_valid():
            try:
            # add logic to update pizza if topping is updated
                pizzaForm.save()
                messages.success(request, "Pizza updated successfully!")
            except Exception as e:
                error_message = e
                messages.error(request, f"An error occured updating the pizza. ERROR: {error_message}")

        return redirect("starting-page")

    return render(request, "pizza/pizza_edit_form.html", context)



def deletePizzaView(request, pk):
    pizza = Pizza.objects.get(id=pk)

    context = {
        "obj": pizza
    }

    if request.method == "POST":
        try:
            pizza.delete()
            messages.success(request, "Pizza was deleted successfully!")

        except Exception as e:
            error_message = e
            messages.error(
                request, f"An error occured updating the topping. ERROR: {error_message}")

        return redirect("starting-page")

    return render(request, "pizza/delete.html", context)


def deletePizzaToppingView(request, pk):
    pizza_topping = PizzaTopping.objects.filter(id=pk)
    # pizza = Pizza.objects.filter(pizza=pizza)

    print("pizza topping:", pizza_topping.query)
    try:
        pizza_topping.delete()
        
        messages.success(request, "Pizza topping was removed successfully!")
        # return redirect("pizza-detail")
        # return redirect("staring-page")

    except Exception as e:
        error_message = e
        messages.error(request, f"An error occured removing the pizza topping. ERROR: {error_message}")

    return render(request, "pizza/pizza_detail.html")

