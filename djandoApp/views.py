from django.shortcuts import render, get_object_or_404
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

def detalle_grupo(request, pk):
	grupo = Grupo_artista.objects.get(id=pk)
	plantilla = loader.get_template("detalle_grupo.html")
	contexto = {
		'grupo':grupo,
	}	
	return HttpResponse(plantilla.render(contexto,request))