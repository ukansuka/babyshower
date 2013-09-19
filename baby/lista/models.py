from django.db import models

class Categoria(models.Model):
	name = models.CharField(max_length=200) 

class Regalo(models.Model): 
	titulo = models.CharField(max_length=200) 
	contenido = models.TextField() 
	imagen = models.TextField()
	asignado = models.BooleanField(default=False)
	categoria = models.ForeignKey(Categoria) 
