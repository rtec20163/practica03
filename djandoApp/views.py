from django.shortcuts import render
from .models import Grupo_artista
from .models import Genero
from django.template import loader
from django.http import HttpResponse


def consultar_grupos(request):
	contenido = Grupo_artista.objects.all()

	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
	}
	return HttpResponse(plantilla.render(contexto,request))
