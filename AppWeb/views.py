from django.shortcuts import render


def home(request):

    return render(request, "AppWeb/home.html")


def tienda(request):

    return render(request, "AppWeb/tienda.html")