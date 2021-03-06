from unicodedata import name
from django.urls import path
from Usuarios.views import PassR, Perfil, Admin, Notification, CreateUser, UpdateUser,EditarPerfil, CambiarEstadoUsuario, Change
urlpatterns = [
    path('RecuperarContrase├▒a/', PassR, name="RecuperarContrase├▒a"),
    path('CambiarContrase├▒a/', Change, name="Cambiar"),
    path('estado/', CambiarEstadoUsuario, name="editarEstadoUsuario"),
    path('Perfil', Perfil, name="Perfil"),
    path('Administracion/', Admin, name="Administracion"),
    path('Notificaciones/', Notification, name="Notify"),
    path('CrearUsuario/', CreateUser.as_view(), name="CreateUser"),
    path('CrearUsuario/<int:pk>', UpdateUser.as_view(), name="UpdateUser"),
    path('EditarPerfil/', EditarPerfil, name="EditarPerfil")
    # path('', Usertoken.as_view(), name = "refresh_token"),
]