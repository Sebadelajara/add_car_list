from django.db import models

# Create your models here.
CATEGORIAS = [
        ('fiat', 'Fiat'),
        ('chevrolet', 'Chevrolet'),
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
    ]
CATEGORIAS2 = [
        ('particular', 'Particular'),
        ('transporte', 'Transporte'),
        ('carga', 'Carga'),
    ]
class Vehiculo(models.Model):
    
    marca = models.CharField(max_length=20, choices=CATEGORIAS, default='ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS2, default='particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.marca} {self.modelo} {self.serial_carroceria} {self.serial_motor} {self.categoria} {self.precio} {self.fecha_creacion} {self.fecha_modificacion}'


