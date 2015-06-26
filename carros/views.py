from django.shortcuts import render
from django.http import HttpResponse
from .models import Marca, Carro
from .forms import AgregarMarcaForm
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class CarroList(ListView):
    model = Carro
    context_object_name = 'carros'


def listar_carros(request):
    carros = Carro.objects.all()
    data = {
        'carros': carros,
    }
    return render(request, "carros.html", data)


def listar_marcas(request):
    marcas = Marca.objects.all()
    data = {
        'marcas': marcas,
    }
    return render(request, "marcas.html", data)


class MarcaCreate(CreateView):
    model = Marca
    template_name = 'agregar_marca.html'
    success_url = reverse_lazy('listar_marcas')
    fields = ['nombre']

    def get_success_url(self):
        messages.success(self.request, 'Marca agregada exitosamente!')
        return super(MarcaCreate, self).get_success_url()


def agregar_marca(request):
    if request.method == "POST":
        form = AgregarMarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Marca Agregada")
    else:
        form = AgregarMarcaForm()
    data = {
        'form': form
    }
    return render(request, "agregar_marca.html", data)
