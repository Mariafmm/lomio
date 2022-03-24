#-----------------------------------------Importaciones---------------------------------------------------
from contextlib import redirect_stderr
from django.http import HttpResponse
from django.template import Template, Context, loader 
from django.shortcuts import render
from Usuarios.views import *
from Usuarios.authentication_mixins import Authentication
from django.views.generic import View
from Configuracion.forms import CambiosForm, FooterForm
from Configuracion.models import cambios, cambiosFooter
from rest_framework.views import APIView
from Usuarios.models import Usuario
#--------------------------------------Cargadores de templates------------------------------------
class Inicio(View):
    def get(self, request, *args, **kwargs):  
        try:
            if request.session:
                print(request.session)
                imagen = Usuario.objects.get(id_usuario=request.session['pk'])
                imagen = imagen.img_usuario
                UserSesion = {"username":request.session['username'], "rol":request.session['rol'], "imagen":imagen, "admin":request.session['Admin']}
            return render(request, 'index.html', {'User':UserSesion})
        except:
            return render(request, 'index.html')
            
class menu(View):
    def get(self, request, *args, **kwargs):
        formulario = CambiosForm
        formulario2 = FooterForm
        Listarfooter =cambiosFooter.objects.all()
        ListarCambios = cambios.objects.all()
        mensaje = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,],'Cambios' :ListarCambios, 'footer' :Listarfooter
        }
        return render(request, 'index.html', mensaje)
    
def SinPermisos(request):
    return render(request, "SinPermisos.html")

def Noregistrado(request):
    return render(request, "NoRegistrado.html")
