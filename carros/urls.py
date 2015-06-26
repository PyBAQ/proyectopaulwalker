#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.listar_carros, name="listar_carros"),
    url(r'^$', views.CarroList.as_view(), name="listar_carros"),
    url(r'^marcas/$', views.listar_marcas, name="listar_marcas"),
    # url(r'^marcas/agregar/$', views.agregar_marca, name="agregar_marca"),
    url(r'^marcas/agregar/$', views.MarcaCreate.as_view(), name="agregar_marca"),
]
