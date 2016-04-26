from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.template import loader
from django.http import *
from .forms import UsuarioForm
from django.contrib import *


def consultar_grupos(request):
	contenido = Grupo_artista.objects.all()
	public = publicacion.objects.all()
	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
		'public':public,
	}
	return HttpResponse(plantilla.render(contexto,request))


###
def detalle_public(request,pk):
	public = get_object_or_404(publicacion,id=1)
	plant = loader.get_template("detalle_public.html")
	contexto = {
		'public':public,
	}
	return HttpResponse(plant.render(contexto,request))

###


def detalle_grupo(request,pk):
	grupo = get_object_or_404(Grupo_artista,id=pk)
	public = publicacion.objects.filter(grupo=pk)#publicacion.objects.get(grupo = grupo.nombre)
	#ob_list = publicacion.objects.filter(Q(name__contains=word))
	plantilla = loader.get_template("detalle_grupo.html")
	contexto = {
		'grupo':grupo,
		'public':public,
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

def login(request):
		username = request.POST.get('username','Hola')
		password = request.POST.get('password','inseguro')
		user = auth.authenticate(username=username, password=password)
		form = UsuarioForm(request.POST)

		if user is not None and user.is_activate:
			auth.login(request, user)

			return render(request,'index.html',{'form':form})

		else:
			return render(request,'login.html',{'form':form})

def logout(request):
	auth.logout(request)

	return render(request,'index.html')








