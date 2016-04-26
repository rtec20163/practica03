from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.consultar_grupos, name='grupos'),
	url(r'^grupo_artista/(?P<pk>[0-9]+)/$', views.detalle_grupo),
	url(r'^registro/$',views.registro,name='registro'),
	url(r'^logiin/$',views.logiin,name='login'),
	url(r'^ingresar/$',views.ingresar),
	url(r'^loogin/$',views.loogin),
]           				