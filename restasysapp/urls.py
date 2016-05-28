from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^mesa/novo/$', views.mesa_novo, name='mesa_novo'),
    url(r'^prato/novo/$', views.prato_novo, name='prato_novo'),
    url(r'^pedido/novo/$', views.pedido_novo, name='pedido_novo'),


]
