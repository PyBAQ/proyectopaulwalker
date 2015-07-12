from django.core.urlresolvers import reverse

from django.test.testcases import TestCase


class FixtureTest(TestCase):

    fixtures = ['marca.json']

    def test_view_list(self):
        response = self.client.get(reverse("listar_marcas"))
        self.assertEqual(response.context['list'].count(), 3)
