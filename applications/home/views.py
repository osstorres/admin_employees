from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  )
from .models import Prueba
from .forms import PruebaForm
# Create your views here.


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaList(ListView):
    queryset = ['0', '10', '20', '30']
    template_name = 'home/lista.html'
    context_object_name = 'lista_numeros'


class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreate(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = '/'