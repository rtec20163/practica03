from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
	username = models.CharField(max_length=32,unique=True)
	password = models.CharField(max_length=32)

	def __str__(self):
		return self.username


class Genero(models.Model):
	nombre = models.CharField(max_length=64)

	def __str__(self):
		return self.nombre

class Grupo_artista(models.Model):
	nombre = models.CharField(max_length=256,unique=True)
	integrantes = models.CharField(max_length=512)
	fecha_inicio = models.DateTimeField()
	genero = models.ManyToManyField(Genero)

	def __str__(self):
		return self.nombre


class Album(models.Model):
	grupo_artista = models.ForeignKey(Grupo_artista, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=128)
	canciones = models.CharField(max_length=512)
	fecha_lanzamiento = models.DateTimeField()

	def __str__(self):
		return self.nombre


class publicacion(models.Model):
	titulo = models.CharField(max_length=256)
	texto = models.TextField()
	autor = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	grupo = models.ForeignKey(Grupo_artista,on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo
