from django.db import models

# Create your models here.
"""
Agrupacion:Nulos, Blancos, Impugnados
"""

class Info_Http(models.Model):
    ubigeo = models.ForeignKey('UbiGeo')
    post_code = models.CharField( max_length=20 )

class Locales(models.Model):
    local = models.ForeignKey('UbiGeo')
    direccion = models.CharField( max_length 360)

class UbiGeo(models.Model):
    OPCIONES_TIPO= (
        ('departamento','Departamento'),
        ('provincia','Provincia'),
        ('distrito','Distrito'),
        ('local','Local')
        )
    nombre = models.CharField( max_length= 120 )
    tipo = models.CharField( max_length = 60, choices=OPCIONES_TIPO )
    parent = models.ForeignKey('self')

class Info_Electoral(models.Model):
    num_mesa = models.IntegerField()
    local = models.ForeignKey('UbiGeo')
    departamento = models.ForeignKey('UbiGeo')
    provincia = models.ForeignKey('UbiGeo')
    local = models.ForeignKey('UbiGeo')

class voto_congresal(models.Model):
    proceso = models.CharField( max_length = 120 )
    agrupacion = models.CharField( max_length = 120 )
    estado_del_acta = models.CharField( max_length = 60 )
    electores_habiles = models.IntegerField()
    electores_que_votaron = models.IntegerField()
    total = models.IntegerField()
    candidato_1 = models.IntegerField()
    candidato_2 = models.IntegerField(null=True)
    candidato_3 = models.IntegerField(null=True)
    candidato_4 = models.IntegerField(null=True)
    candidato_5 = models.IntegerField(null=True)
    candidato_6 = models.IntegerField(null=True)
    candidato_7 = models.IntegerField(null=True)
    candidato_8 = models.IntegerField(null=True)
    candidato_9 = models.IntegerField(null=True)
    candidato_10 = models.IntegerField(null=True)
    candidato_11 = models.IntegerField(null=True)
    candidato_12 = models.IntegerField(null=True)
    candidato_13 = models.IntegerField(null=True)
    candidato_14 = models.IntegerField(null=True)
    candidato_15 = models.IntegerField(null=True)
    candidato_16 = models.IntegerField(null=True)
    candidato_17 = models.IntegerField(null=True)
    candidato_18 = models.IntegerField(null=True)
    candidato_19 = models.IntegerField(null=True)
    candidato_20 = models.IntegerField(null=True)
    candidato_21 = models.IntegerField(null=True)
    candidato_22 = models.IntegerField(null=True)
    candidato_23 = models.IntegerField(null=True)
    candidato_24 = models.IntegerField(null=True)
    candidato_25 = models.IntegerField(null=True)
    candidato_26 = models.IntegerField(null=True)
    candidato_27 = models.IntegerField(null=True)
    candidato_28 = models.IntegerField(null=True)
    candidato_29 = models.IntegerField(null=True)
    candidato_30 = models.IntegerField(null=True)
    candidato_31 = models.IntegerField(null=True)
    candidato_32 = models.IntegerField(null=True)
    candidato_33 = models.IntegerField(null=True)
    candidato_34 = models.IntegerField(null=True)
    candidato_35 = models.IntegerField(null=True)
    candidato_36 = models.IntegerField(null=True)


"""
class voto_presidencial(models.Model):
    proceso = 
    num_mesa = 
    estado_del_acta = models.CharField( max_length = 60 )
    votos_emitidos = models.IntegerField()
    agrupacion = models.CharField( max_length = 60 )
"""
