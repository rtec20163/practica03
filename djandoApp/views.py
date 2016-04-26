from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.template import loader
from django.http import *
from .forms import UsuarioForm
from django.contrib import *
from django.contrib.auth import *



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

from django.core.urlresolvers import reverse
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)      

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect('/accounts/invalid')

def logiin(request):
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username, password=password)
		

		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')

		else:
			return HttpResponseRedirect('/logiin.html')

def logout(request):
	auth.logout(request)

	return render(request,'index.html')


def ingresar(request):
	if request.method =='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect(request,'index.html')
				else:
					return render_to_response('index.html', contex_instance = RequestContext(request))
	else:
		formulario = AuthenticationForm() ## error
	return render_to_response('index.html',{'formulario':formulario},contex_instance=RequestContext(request))
				
def loogin(request):
	if request.method =='POST':
		formulario = LoginForm(request.POST)
		if formulario.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			acceso = authenticate(username=usuario,password=clave)
			if acceso is not None:
				login(request,acceso)
				return HttpResponseRedirect('index')
			else:
				return render_to_response('loogin.html',{'form':form},contex_instance=RequestContext(request))
		else:
			return render_to_response('loogin.html',{'form':form},contex_instance=RequestContext(request))
	else:
		form = LoginForm()## aqui error 
		contexto = {'form':form}
		return render_to_response('loogin.html',contexto,contex_instance=RequestContext(request))
















