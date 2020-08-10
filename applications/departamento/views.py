from django.shortcuts import render
from .forms import NewDepartamentoForm
from django.views.generic.edit import FormView
# Create your views here.
from django.urls import reverse_lazy
from applications.persona.models import Empleado
from .models import Departamento

class NewDepartamento(FormView):
    form_class = NewDepartamentoForm
    template_name = 'departamento/new_departamento.html'
    success_url = reverse_lazy('persona_app:empleados')

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )

        return super(NewDepartamento, self).form_valid(form)