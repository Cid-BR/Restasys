from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^mesa/novo/$', views.mesa_novo, name='mesa_novo'),
    url(r'^prato/novo/$', views.prato_novo, name='prato_novo'),
    url(r'^pedido/novo/$', views.pedido_novo, name='pedido_novo'),
    url(r'^mesa/list/$', views.mesa_list, name='mesa_list'),
    url(r'^pratos/list/$', views.pratos_list, name='pratos_list'),
    url(r'^pedidos/list/$', views.pedidos_list, name='pedidos_list'),
    url(r'^mesa/(?P<pk>[0-9]+)/$', views.mesa_detalhe),

]
