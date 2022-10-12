from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pizza, Topping, Cart


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        exclude = []

# class PizzaForm(forms.Form):
#     name = forms.CharField()
#     toppings = forms.CharField()
#     extra_field_count = forms.CharField(widget=forms.HiddenInput())

#     def __init__(self, *args, **kwargs):
#         extra_fields = kwargs.pop('extra', 0)

#         super(PizzaForm, self).__init__(*args, **kwargs)
#         self.fields['extra_field_count'].initial = extra_fields

#         for index in range(int(extra_fields)):
#             # generate extra fields in the number specified via extra_fields
#             self.fields['extra_field_{index}'.format(index=index)] = \
#                 forms.CharField()


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
