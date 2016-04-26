from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.consultar_grupos, name='grupos'),
	url(r'^grupo_artista/(?P<pk>[0-9]+)/$', views.detalle_grupo),
	url(r'^grupo_public/(?P<pk>[0-9]+)/$', views.detalle_public),
	url(r'^registro/$',views.registro,name='registro'),
	url(r'^comentar/$',views.comentar,name='comentar'),
	url(r'^login/$',views.login,name='login'),
	url(r'^lista_publicaciones/$',views.detalle_public,name='lista_publicaciones'),
]