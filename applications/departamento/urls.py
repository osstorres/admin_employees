from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento'
urlpatterns = [
    path('nuevo-departamento/', views.NewDepartamento.as_view(), name = 'nuevodepartamento')
]