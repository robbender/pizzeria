from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.startingPage, name="starting-page"),
    path("topping-form", views.toppingFormView, name="topping-form"),
    path("update-topping/<str:pk>", views.updateToppingFormView, name="update-topping"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)