from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext, loader, Context, Template
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login, logout
from django.http import *


def consultar_grupos(request):
	contenido = Grupo_artista.objects.all()

	plantilla = loader.get_template("index.html")
	contexto = {
		'contenido':contenido,
	}
	return HttpResponse(plantilla.render(contexto,request))

