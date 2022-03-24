"""Proyecto_Ekiria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Proyecto_Ekiria.views import Inicio, menu, SinPermisos, Noregistrado
from Usuarios.views import Login, Register, Loguot
from rest_framework.authtoken import views

urlpatterns = [
    path('', Inicio.as_view(), name="Inicio"),
    path('UsuarioNoRegistrado', Noregistrado, name="UNR"),
    path('menu/', menu.as_view(), name="menu"),
    path('IniciarSesion/', Login, name="IniciarSesion"),
    path('CerrarSesion/', Loguot, name="CerrarSesion"),
    path('Registro/', Register.as_view(), name="Registro"),
    path('InformacionUsuario/', include('Usuarios.urls')),
    path('admin/', admin.site.urls),
    path('Inicio/', Inicio),
    path('Ventas/', include ('Ventas.urls')),
    path('Configuracion/', include ('Configuracion.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api_generate_token/', views.obtain_auth_token, name="tokenGenerate"),
    path('SinPermisos/', SinPermisos, name="SinPermisos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

