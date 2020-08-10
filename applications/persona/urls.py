from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "persona_app"
urlpatterns = [
    path('', views.inicioView.as_view(), name='inicio'),
    path('list_all_employees/', views.ListAllEmployees.as_view(), name='empleados'),
    path('listbyarea/<shortname>/', views.ListByAreaEmpleado.as_view()),
    path('listbyjob/<job>/', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('habilidades/', views.ListHabilidades.as_view()),
    path('detail/<pk>/', views.EmpleadoDetail.as_view(),name='empleado_detail'),
    path('create/', views.CreateEmployee.as_view()),
    path('sucess/', views.SucessTemplate.as_view(), name='sucess'),
    path('update_employee/<pk>/', views.UpdateEmployee.as_view(), name='update_employee'),
    path('delete_employee/<pk>/', views.deleteEmpleado.as_view(), name='delete_employee'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)