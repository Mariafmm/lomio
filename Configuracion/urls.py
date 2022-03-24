from unicodedata import name
from django.urls import  path
from . import views

urlpatterns=[
    path("", views.Configuracion, name="Configuracion"),
    path("Roles/", views.ListarRol, name="Roles"),
    path("Cambios/", views.Cambios, name="Cambios"),
    path("Permisos/", views.Permisos, name="Permisos"),
    path("Admin/", views.Admin, name="Admin"),
    path("Empleado/", views.Empleado, name="Empleado"),
    path("Cliente/", views.Cliente, name="Cliente"),
    path("EditarRol/<int:pk>",views.EditarRolView.as_view(), name="updateRol"),
    path("CrearRol/", views.CreateRolView.as_view(), name="CreateRol"),
    path("EstadoRol/",views.EstadoRol, name="estado"),
]
