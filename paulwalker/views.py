from django.http import HttpResponse
from django.shortcuts import render
from carros.forms import AgregarMarcaForm
from carros.models import Marca


def home(request):
    return render(request, "base.html")

def listar_carros(request):
    return render(request, "carros.html")

def listar_marcas(request):
    marcas = Marca.objects.all()
    data = {
        'marcas': marcas
    }
    return render(request, "marcas.html", data)


def agregar_marca(request):
    if request.method == "POST":
        form = AgregarMarcaForm(request.POST)
        if form.is_valid():
            marca = form.save()
            return HttpResponse("Marca Agregada")
    else:
        form = AgregarMarcaForm()
    data = {
        'form': form
    }
    return render(request, "agregar_marca.html", data)



