from django.conf.urls import include, url
from . import views

urlpatterns = [
	#url(r'',views.consultar_grupos, name='grupos'),
	url(r'^ingresar',views.ingresar),
	url(r'^usuario/nuevo',views.nuevo_usuario),
	url(r'^privado/$','principal.views.privado'),
	   url(r'^cerrar/$', 'principal.views.cerrar'),
	#
]