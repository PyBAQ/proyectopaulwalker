import unittest

from django.test import Client
from django.test.testcases import SimpleTestCase
from django.shortcuts import resolve_url

from ..forms import AgregarMarcaForm


class SimpleTest(SimpleTestCase):

    def test_view_list(self):
        response = self.client.get(resolve_url("listar_carros"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "carros/carro_list.html")

    def test_view_create(self):
        response = self.client.get(resolve_url("agregar_marca"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "agregar_marca.html")

    def test_create(self):
        response = self.client.post(resolve_url("agregar_marca"),
                                    {"nombre": "prueba de marca"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "marcas.html")
        marcas = response.context['list']
        self.assertEqual(marcas.count(), 1)

    def test_form_invalid(self):
        form = AgregarMarcaForm()
        self.assertEqual(form.is_valid(), False)

    def test_form(self):
        form = AgregarMarcaForm({"nombre": "esto es un texto"})
        self.assertEqual(form.is_valid(), True)
