from django.shortcuts import render
from .forms import FormularioContacto


def contacto(request):
    
    formulario = FormularioContacto()

    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")

    return render(request, "Contacto/contacto.html", {"formulario": formulario})
