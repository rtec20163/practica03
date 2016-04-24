from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext, loader, Context, Template
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages


def consultar_grupos(request):
	contenido = Grupo_artista.objects.all()

	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
	}
	return HttpResponse(plantilla.render(contexto,request))


@login_required
def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'login.html', {'mensaje': mensaje})




def logout_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('accounts.login'))

def registro_usuario_view(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = Usuario(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
       
            # Ahora, redireccionamos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.
            return redirect(reverse('gracias', kwargs={'username': username}))
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = RegistroUserForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'registro.html', context)


def gracias_view(request, username):
    return render(request, 'gracias.html', {'username': username})
