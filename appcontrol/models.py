from django.db import models
import datetime


class persona (models.Model):
    dni=models.CharField(max_length=8, primary_key=True, verbose_name="DNI")
    apellido_paterno=models.CharField(max_length=200, verbose_name="Apellido paterno", blank=True)
    apellido_materno=models.CharField(max_length=200,verbose_name="Apellido materno", blank=True)
    nombres=models.CharField(max_length=200, verbose_name="Nombres") 
    sexo=models.BooleanField()
    fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento", blank=True)
    ubigeo_nacimiento=models.CharField(max_length=6, blank=True)
    correo_institucional = models.CharField(max_length=200, blank=True,verbose_name="Correo institucional")
    telefono = models.CharField(max_length=9, blank=True, verbose_name="Teléfono")
    def __str__(self):
        return  self.apellido_paterno + " " +self.apellido_materno+ " " +self.nombres


class jefe(models.Model):
     id_jefe = models.AutoField(primary_key=True, verbose_name="Id")
     dni_jefe = models.ForeignKey(persona, on_delete=models.PROTECT, verbose_name="Jefe inmediato",related_name='rf_persona_jefe')
     dni_empleado = models.ForeignKey(persona, on_delete=models.PROTECT, verbose_name="Subordinado",related_name='rf_persona_empleado')
     estado_jefe = models.BooleanField(default=True, blank=True)
     fechahora_creacion=models.DateField(default=datetime.datetime.now, blank=True)
  
     def __str__(self):
        return self.id_jefe


class periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    detalle = models.CharField(max_length=100, verbose_name="Detalle")
    dias_laborables = models.IntegerField(verbose_name="Total de días laborable")
    observacion = models.CharField(max_length=100, verbose_name="Observación", blank=True)
    estado_periodo = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.descripcion



class dependencia (models.Model):
    id_dependencia = models.AutoField(primary_key=True, verbose_name="Id")
    nombre_dependencia = models.CharField(max_length=200, verbose_name="Nombre")
    abreviatura_dependencia = models.CharField(max_length=20, verbose_name="Abreviatura")
    id_dep_tip = models.IntegerField(verbose_name="Id tipo")
    id_sede = models.IntegerField(verbose_name="Id Sede")
    id_depe_superior = models.IntegerField(verbose_name="Id Superior")
    codigo_depe = models.CharField(max_length=8, verbose_name="Código")
    estado_depe = models.BooleanField(default=True, blank=True)
    def __str__ (self):
        return self.nombre_dependencia


class tipoactividad (models.Model):
    id_tipoactividad = models.AutoField(primary_key=True, verbose_name="Id")
    nombre_tipoactividad = models.CharField(max_length=100, verbose_name="Nombre")
    abreviatura_tipoactividad = models.CharField(max_length=20, verbose_name="Abreviatura")

    def __str__(self):
        return self.nombre_tipoactividad


class actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True, verbose_name="Id")
    id_periodo =models.ForeignKey(periodo, on_delete=models.PROTECT)
    id_tipoactividad = models.ForeignKey(tipoactividad, on_delete=models.PROTECT)
    dni = models.ForeignKey(persona, on_delete=models.PROTECT,related_name='rf_persona_empleado_actividad')
    
    telefono =models.CharField(max_length=9, verbose_name="Teléfono", blank=True)
    correo = models.CharField(max_length=100, verbose_name="Correo institucional", blank=True)

    id_dep = models.ForeignKey(dependencia, on_delete=models.PROTECT)
    nombre_dependencia = models.CharField(max_length=200, verbose_name="Dependencia", blank=True)

    gr_comorbilidad = models.BooleanField(verbose_name="Comorbilidad", blank=True)
    detalle_comorbilidad = models.CharField(max_length=200, verbose_name="Detalle comorbilidad", blank=True)
    
    tiene_informe = models.BooleanField(default=True, blank=True, verbose_name="Tiene informe?")
    actividad_resumen = models.CharField(max_length=200, verbose_name="Resumen de actividad", blank=True)
    producto_entregado = models.CharField(max_length=200, verbose_name="Producto entregado", blank=True)
    medio_verificacion = models.CharField(max_length=200, verbose_name="Medio de verificación", blank=True)
    archivo_informe= models.FileField(upload_to="media/docs/informe", null = True)

    modalidad = models.CharField(max_length=200, verbose_name="Modalidad que trabajo", blank=True)
    dias_laborado = models.IntegerField( verbose_name="Dias laborado", blank=True)

    dni_jefe = models.ForeignKey(persona, on_delete=models.PROTECT, related_name='rf_persona_jefe_actividad')
    nombre_jefe = models.CharField(max_length=100, verbose_name="Jefe inmediato", blank=True)
    correo_jefe = models.CharField(max_length=100, verbose_name="Correo de jefe inmediato", blank=True)
    telefono_jefe = models.CharField(max_length=9, verbose_name="Télefono", blank=True)
    documento = models.CharField(max_length=200, verbose_name="Documento de conformidad", blank=True)
    archivo_documento= models.FileField(upload_to="media/docs/documento", null = True)
    observacion  = models.CharField(max_length=200, verbose_name="Observación", blank=True)
    def __str__(self):
        return str(self.id_actividad)







