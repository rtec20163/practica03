from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.template import loader
from django.http import HttpResponse
from .forms import UsuarioForm


def consultar_grupos(request):
	contenido = Grupo_artista.objects.all()

	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
	}
	return HttpResponse(plantilla.render(contexto,request))

def detalle_grupo(request,pk):
	grupo = get_object_or_404(Grupo_artista,id=pk)
	plantilla = loader.get_template("detalle_grupo.html")
	contexto = {
		'grupo':grupo,
	}	
	return HttpResponse(plantilla.render(contexto,request))

def registro(request):
	if request.method =="POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			usuario=form.save(commit=False)
			usuario.save()
			return consultar_grupos(request)
	else:
		form = UsuarioForm()
	return render(request,'registro.html',{'form':form})