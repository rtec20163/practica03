from django.shortcuts import render
from .models import Grupo_artista
from .models import Genero
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def consultar_grupos(request):
	contenido = Grupo_artista.objects.all()

	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
	}
	return HttpResponse(plantilla.render(contexto,request))


def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('index')
	else:
		formulario = UserCreationForm()
	return render_to_respose('nuevo_usuario.html',{'formulario':formulario},contex_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
	usuario=request.user
	return render_to_response('privado.html', {'usuario':usuario}, contex_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')


def  ingresar(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso.is_active:
				login(request,acceso)
				return HttpResponseRedirect('/privado')
			else:
				return render_to_response('noactivo.html', contex_instance=RequestContext(request))
		else:
			return render_to_response('nousuario.html', contex_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('ingresa.html', {'formulario':formulario}, contex_instance=RequestContext(request))

			
