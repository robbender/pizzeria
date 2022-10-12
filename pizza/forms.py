from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Pizza, Topping, Cart


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        exclude = []


class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = '__all__'
        exclude = []


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
        exclude = []
