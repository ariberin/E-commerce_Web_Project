from django.urls import path
from Contacto.views import contacto

urlpatterns = [
    path('', contacto, name="Contacto"),
]