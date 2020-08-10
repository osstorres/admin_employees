from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
)
from .models import Empleado
from django.urls import reverse_lazy

# Create your views here.
class inicioView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmployees(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    model = Empleado
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListByAreaEmpleado(ListView):
    template_name = 'persona/listarea.html'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area)
        return lista


class ListByJobEmpleado(ListView):
    template_name = 'persona/list_job.html'

    def get_queryset(self):
        job = self.kwargs['job']
        lista = Empleado.objects.filter(
            job=job)
        return lista


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        kword = self.request.GET.get("kword","")
        element = Empleado.objects.filter(first_name=kword)
        return element


class ListHabilidades(ListView):
    template_name = 'persona/listhabilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        habilidades = Empleado.objects.get(id=5)
        return habilidades.all()


class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = 'persona/detailempleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetail, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SucessTemplate(TemplateView):
    template_name = "persona/sucess.html"


class CreateEmployee(CreateView):
    model = Empleado
    template_name = "persona/create_empleado.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(CreateEmployee, self).form_valid(form)


class UpdateEmployee(UpdateView):
    model = Empleado
    template_name = "persona/update_employee.html"
    fields = [
        'first_name',
        'last_name',
        'job'
    ]
    success_url = reverse_lazy('persona_app:empleados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(UpdateEmployee, self).form_valid(form)


class deleteEmpleado(DeleteView):
    model = Empleado
    template_name = "persona/delete_employee.html"
    success_url = reverse_lazy('persona_app:empleados')

