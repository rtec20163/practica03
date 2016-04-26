from django import forms

from .models import Usuario , publicacion

class UsuarioForm(forms.ModelForm):

	class Meta:
		model=Usuario
		fields=('username','password',)

class PublicacionForm(forms.ModelForm):

	class Meta:
		model=publicacion
		fields=('titulo','texto','autor','grupo')
