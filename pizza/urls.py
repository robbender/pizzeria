from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.startingPage, name="starting-page"),
    path("topping-form", views.toppingFormView, name="topping-form"),
    path("update-topping/<str:pk>", views.updateToppingFormView, name="update-topping"),
    path("delete-topping/<str:pk>", views.deleteToppingView, name="delete-topping"),
    path("delete-pizza-topping/<str:pk>", views.deletePizzaToppingView, name="delete-pizza-topping"),
    path("pizza-form", views.pizzaFormView, name="pizza-form"),
    path("pizza-detail/<str:pk>", views.pizzaDetail, name="pizza-detail"),
    path("update-pizza/<str:pk>", views.updatePizzaFormView, name="update-pizza"),
    path("delete-pizza/<str:pk>", views.deletePizzaView, name="delete-pizza"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)