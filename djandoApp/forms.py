from django import forms

from .models import Usuario, publicacion, Grupo_artista, Genero

class UsuarioForm(forms.ModelForm):

	class Meta:
		model=Usuario
		fields=('username','password')

class PublicacionForm(forms.ModelForm):

	class Meta:
		model=publicacion
		fields=('titulo','texto','autor','grupo')

class GrupoForm (forms.ModelForm):
	class Meta:
		model = Grupo_artista
		fields=('nombre','integrantes','genero','fecha_inicio')

class GeneroForm (forms.ModelForm):
	class Meta:
		model = Genero
		fields=('nombre',)

