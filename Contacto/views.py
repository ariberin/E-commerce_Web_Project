from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage


def contacto(request):
    
    formulario = FormularioContacto()

    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")

            email = EmailMessage("Mensaje desde Hype Market Web", 
            "El usuario {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, mensaje),
            "",["berinsteina@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, "Contacto/contacto.html", {"formulario": formulario})
