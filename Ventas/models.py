from typing_extensions import Required
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse 
from django.conf import settings

usuario=settings.AUTH_USER_MODEL


# modelo para administrar los tipos de servicios
class Tipo_servicio(models.Model):
    id_tipo_servicio=models.AutoField("Id del Tipo de Servicio", primary_key=True, unique=True)
    nombre=models.CharField("Nombre", max_length=50, null=False,blank=False, unique=True)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'tipo_servicios'
        verbose_name = 'tipo de servicio'
        verbose_name_plural = 'tipo_servicios'

    def __str__(self):
        return self.nombre

# modelo para administrar los servicios
class Servicio(models.Model):
    id_servicio=models.AutoField("Id del Servicio", primary_key=True, unique=True)
    slug=models.SlugField("Slug", unique=True)
    nombre=models.CharField("Nombre", max_length=40, null=False, blank=False, unique=True)
    descripcion=models.TextField("Descripcion",null=False,blank=False)
    img_servicio=models.ImageField("Imagen del Servicio", upload_to='Ventas/servicios',null=False, blank=False)
    precio=models.IntegerField("Precio",null=False, blank=False)
    tipo_servicio_id=models.ForeignKey(Tipo_servicio, verbose_name="Tipo de Servicio", on_delete=models.CASCADE,null=True, blank=True, db_column="tipo_servicio_id")
    duracion=models.PositiveIntegerField(default=0)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'servicios'
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Ventas:detalleSer", kwargs={"slug": self.slug})

   
    

# modelo para administrar el catalogo
class Catalogo(models.Model):
    id_catalogo=models.AutoField("Id del Catalogo", primary_key=True, unique=True)
    servicio_id=models.ForeignKey(Servicio, verbose_name="Servicio", on_delete=models.CASCADE,null=True, blank=True,db_column="servicio_id")
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'catalogo'
        verbose_name = 'catalogo'
        ordering = ['id_catalogo','servicio_id','fecha_creacion','fecha_actualizacion','estado']

    def __str__(self):
        return str(self.servicio_id.id_servicio)

# modelo para administrar los servicios personalizados     
class Servicio_Personalizado(models.Model):
    id_servicio_personalizado=models.AutoField("Id del Servicio Personalizado", primary_key=True, unique=True)
    descripcion=models.TextField("Descripcion",null=True,blank=True)
    img_servicio=models.ImageField("Imagen del Servicio", upload_to="Ventas/servicios_personalizados",null=False, blank=False)
    precio=models.IntegerField("Precio",null=True, blank=True)
    tipo_servicio_id=models.ForeignKey(Tipo_servicio, verbose_name="Tipo de Servicio", on_delete=models.CASCADE,null=False, blank=False, db_column="tipo_servicio_id")
    duracion=models.PositiveIntegerField(default=0)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'servicios_personalizados'
        verbose_name = 'servicio personalizado'
        verbose_name_plural = 'servicios_personalizados'

    def __str__(self):
        c_servicio=f"El servicio personalizado es: {self.descripcion}"
        return c_servicio

# modelos para administrar los pedidos
class Pedido(models.Model):
    id_pedido=models.AutoField("Id del Pedido", primary_key=True, unique=True)
    cliente_id=models.ForeignKey(usuario, on_delete=models.SET_NULL, blank=True, null=True, db_column="cliente_id")
    completado=models.BooleanField(default=False, null=True, blank=False)
    # total_pagar=models.IntegerField("Total a pagar",null=False,blank=False)
    
    esPersonalizado=models.BooleanField("Es personalizado", default=False)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f"el id del pedido es: {self.id_pedido}"

    @property
    def get_total_carrito(self):
        itemspedido = self.pedidoitem_set.all()
        total = sum([item.get_total for item in itemspedido])
        return total 

    @property
    def get_items_carrito(self):
        itemspedido = self.pedidoitem_set.all()
        total = sum([item.cantidad for item in itemspedido])
        return total 


    
    

# modelos para administrar los items del pedido
class PedidoItem(models.Model):
    id_pedidoItem=models.AutoField("Id del Item del  Pedido", primary_key=True, unique=True)
    servicio_id=models.ForeignKey(Servicio, verbose_name="Id del Servicio",db_column="servicio_id", on_delete=models.SET_NULL, null=True)
    servicio_personalizado_id=models.ForeignKey(Servicio_Personalizado, verbose_name="Servicios Personalizados",on_delete=models.SET_NULL, null=True,db_column="servicio_personalizado_id")
    cantidad=models.IntegerField("Cantidad", default=1, null=True, blank=True)
    pedido_id=models.ForeignKey(Pedido, verbose_name="Id del Pedido",db_column="pedido_id", on_delete=models.SET_NULL, null=True)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'pedidoItems'
        verbose_name = 'pedidoItem'
        verbose_name_plural = 'pedidoItems'

    def __str__(self):
        return f"el id del pedido es: {self.id_pedidoItem}"

    @property
    def get_total(self):
        try:
            total = self.servicio_id.precio * self.cantidad
        except Exception as e:
            print(str(e))
            total=0
        return total

    
    
    

# modelos para administrar los pedidos personalizados osea que tenga por lo menos un servicio personalizado
class Pedido_Personalizado(models.Model):
    id_pedido_personalizado=models.AutoField("Id del Pedido Personalizado", primary_key=True, unique=True)
    servicio_id=models.ForeignKey(Servicio, verbose_name="Id del Servicio",db_column="servicio_id", on_delete=models.SET_NULL, null=True)
    servicio_personalizado_id=models.ForeignKey(Servicio_Personalizado, verbose_name="Servicios Personalizados",on_delete=models.SET_NULL, null=True,db_column="servicio_personalizado_id")
    cantidad=models.IntegerField("Cantidad", default=1, null=True, blank=True)
    pedido_id=models.ForeignKey(Pedido, verbose_name="Id del Pedido",db_column="pedido_id", on_delete=models.SET_NULL, null=True)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)


    class Meta:
        db_table = 'pedidos_personalizados'
        verbose_name = 'pedido personalizado'
        verbose_name_plural = 'pedidos_personalizados'

    def __str__(self):
        return f"el id del pedido personalizado es: {self.id_pedido_personalizado}"

class Cita(models.Model):
    id_cita=models.AutoField("Id de la Cita", primary_key=True, unique=True)
    empleado_id=models.ForeignKey(usuario, on_delete=models.SET_NULL, blank=True, null=True, db_column="empleado_id", related_name="empleado_id")
    cliente_id=models.ForeignKey(usuario, on_delete=models.SET_NULL, blank=True, null=True, db_column="cliente_id",related_name="cliente_id")
    pedido_id=models.ForeignKey(Pedido, verbose_name="Id del Pedido",db_column="pedido_id", on_delete=models.SET_NULL, null=True)
    diaCita=models.DateField("Dia de la cita")
    horaInicioCita=models.TimeField("Fecha de Inicio de la Cita")
    horaFinCita=models.TimeField("Fecha de Fin de la Cita")
    descripcion=models.TextField("Descripcion",null=True ,blank=True)
    fecha_creacion=models.DateField("Fecha de Creacion", auto_now=False, auto_now_add=True)
    fecha_actualizacion= models.DateTimeField("Fecha de Actualizacion", auto_now=True, auto_now_add=False)
    estado=models.BooleanField("Estado", default=True)

    class Meta:
        db_table = 'citas'
        verbose_name = 'cita'
        verbose_name_plural = 'citas'

    def __str__(self):
        return f"el cliente de esta cita es: {self.cliente_id}"

class Calendario(models.Model):
    empleado_id=models.ForeignKey(usuario, on_delete=models.SET_NULL,null=True, db_column="empleado_id", related_name="empleado_calendario_id")
    cliente_id=models.ForeignKey(usuario, on_delete=models.SET_NULL,null=True, db_column="cliente_id",related_name="cliente_calendario_id")
    cita_id=models.ForeignKey(Cita, on_delete=models.SET_NULL,null=True,db_column="cita_id")
    dia=models.DateField(null=False, blank=False)
    horaInicio=models.TimeField(null=False, blank=False)
    horaFin=models.TimeField(null=False, blank=False)

    class Meta:
        db_table = 'calendario'
        verbose_name = 'calendario'
        verbose_name_plural = 'calendario'

    def __str__(self):
        return f"el cliente de esta cita es: {self.cliente_id}"

def pre_save_servicio_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.nombre)

pre_save.connect(pre_save_servicio_receiver,sender=Servicio)
