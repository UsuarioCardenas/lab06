from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('fecha de registro',auto_now=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    imagen = models.CharField(max_length=200, null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre
