from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.template import loader
from django.http import *
from .forms import GrupoForm, UsuarioForm, PublicacionForm, GeneroForm
from django.contrib import *


def consultar_grupos(request):
	contenido = Grupo_artista.objects.order_by('nombre')#ORDENA LOS GRUPOS POR NOMBRE
	public = publicacion.objects.order_by('id')#ORDENA POR ID PARA EL PASO SIGUIENTE
	public = public.reverse()[:5]#MUESTRA LOS ULTIMOS 5 POST CREADOS
	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
		'public':public,
	}
	return HttpResponse(plantilla.render(contexto,request))

###
def detalle_public(request,pk):
	public = get_object_or_404(publicacion,id=pk)
	plant = loader.get_template("detalle_public.html")
	contexto = {
		'public':public,
	}
	return HttpResponse(plant.render(contexto,request))
###


def detalle_grupo(request,pk):
	grupo = get_object_or_404(Grupo_artista,id=pk)
	public = publicacion.objects.filter(grupo=pk)
	public = public.order_by('id')
	public = public.reverse()

	formUNO = PublicacionForm(request.POST)
	if request.method == "POST":
		if formUNO.is_valid():
			publica=formUNO.save(commit=False)
			publica.save()
			return redirect('http://127.0.0.1:8000/grupo_artista/'+ pk)
	else:
		formUNO = PublicacionForm()
	contexto = {
		'grupo':grupo,
		'public':public,
		'formUNO':formUNO,
	}	

	plantilla = loader.get_template("detalle_grupo.html")
	return HttpResponse(plantilla.render(contexto,request))
####
def comentar(request):
	if request.method =="POST":
		formUNO = PublicacionForm(request.POST)
		if formUNO.is_valid():
			publicacion=formUNO.save(commit=False)
			publicacion.save()

			return redirect('http://127.0.0.1:8000/')
	else:
		formUNO = PublicacionForm()
	return render(request,'comentar.html',{'formUNO':formUNO})

####
def registro(request):
	if request.method =="POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			usuario=form.save(commit=False)
			usuario.save()
			return redirect('http://127.0.0.1:8000/')
	else:
		form = UsuarioForm()
	return render(request,'registro.html',{'form':form})

def registro_grupo(request):
	if request.method =="POST":
		form = GrupoForm(request.POST)
		if form.is_valid():
			grupo=form.save(commit=False)
			grupo.save()
			return redirect('http://127.0.0.1:8000/')
	form = GrupoForm()
	formUNO = GeneroForm(request.POST)
	if formUNO.is_valid():
		genero=formUNO.save(commit=False)
		genero.save()
		return redirect('http://127.0.0.1:8000/registro_grupo/')
	else:
		formUNO = GeneroForm()
	return render(request,'registro_grupo.html',{'form':form,'formUNO':formUNO})

def registro_genero(request):
	if request.method =="POST":
		form = GeneroForm(request.POST)
		if form.is_valid():
			genero=form.save(commit=False)
			genero.save()
			return redirect('http://127.0.0.1:8000/')
	else:
		form = GeneroForm()
	return render(request,'registro_genero.html',{'form':form})

def login(request):
	if request.method == 'POST':
		print "consuta"
		form =UsuarioForm(request.POST)

		try:
			r= Usuario.objects.get(username=request.POST['username'])
			
		except Exception, e:
			print "ecepcion"
			print e

		print "el usuario: "
		print r 
		print "su password: "
		print r.password
		print "su id: "
		print r.id
		v = request.POST['password']
		print "lo que escribio: "
		print v


		if r.password == v:
			print "paso"
			request.session['member_id']=r.id
			
			return redirect('http://127.0.0.1:8000/')
		else:
			
			return redirect('login')
	else:
		print "sino es  un usuario"
		form = UsuarioForm()
	print "no paso"
	return render(request,'login.html',{'form':form})

	

	

def logout(request):
	try:
		del request.session['member_id']
	except KeyError:
		pass
	return HttpResponse('has cerrado session')




