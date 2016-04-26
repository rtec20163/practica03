from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.consultar_grupos, name='grupos'),
	url(r'^grupo_artista/(?P<pk>[0-9]+)/$', views.detalle_grupo),
	url(r'^registro/$',views.registro,name='registro'),
	url(r'^publicacion/new/$',views.publicacion_nueva, name='publicacion_nueva'),
	url(r'^registro_grupo/$',views.registro_grupo,name='registro_grupo'),

]           