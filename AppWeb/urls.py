from django.contrib import admin
from django.urls import path, include
from AppWeb.views import home, tienda, contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="Home"),
    path('tienda/', tienda, name="Tienda"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)