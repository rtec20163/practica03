from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'',views.consultar_grupos, name='grupos'),
	url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'gracias/(?P<username>[\w]+)/$',views.gracias_view,name='accounts.gracias'),
    url(r'^$', views.index_view, name='accounts.index'),
    url(r'^login/$', views.login_view, name='accounts.login'),
	
]