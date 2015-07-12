import unittest
from django.core.urlresolvers import reverse

from django.test import Client
from django.test.testcases import TransactionTestCase
from django.shortcuts import resolve_url

from ..models import Marca


class TransactionTest(TransactionTestCase):

    def test_create_marca(self):
        response = self.client.post(resolve_url("agregar_marca"),
                                    {"nombre": "prueba de marca"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "marcas.html")
        marcas = response.context['list']
        self.assertEqual(marcas.count(), 1)

    def test_models_str(self):
        marca = Marca()
        marca.nombre = "test1"
        marca.save()
        self.assertEqual(str(marca), marca.nombre)
