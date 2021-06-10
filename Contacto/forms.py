from django.forms import *


class FormularioContacto(forms.Form):
    
    nombre = CharField(label='Nombre', required=True, max_length=30)
    email = CharField(label='Email', required=True)
    mensaje = CharField(label="Mensaje", widget=Textarea)
