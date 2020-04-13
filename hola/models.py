from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    fec_nac = models.DateField()

    def __str__(self):
            return self.nombre
    
