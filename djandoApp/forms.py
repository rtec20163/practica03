from django import forms

from .models import Usuario
from .models import publicacion
from .models import Grupo_artista

class UsuarioForm(forms.ModelForm):

	class Meta:
		model=Usuario
		fields=('username','password',)

class PostForm(forms.ModelForm):		

	class Meta1:
		model = publicacion 
		fields = ('titulo', 'texto')

class GrupoForm(forms.ModelForm):

	class Meta:
		model= Grupo_artista
		fields=('nombre','integrantes','genero',)		