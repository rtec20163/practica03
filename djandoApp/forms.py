from django import forms
from django.contrib.auth.models import User


class RegistroUserForm(forms.Form):

    username = forms.CharField(min_length=5)
    password = forms.CharField(min_length=5, widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    

    def clean_username(self):
        
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

   
    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2
