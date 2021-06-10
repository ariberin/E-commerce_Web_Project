from django.shortcuts import render
from .forms import FormularioContacto


def contacto(request):
    
    formulario = FormularioContacto()

    return render(request, "Contacto/contacto.html", {"formulario": formulario})
