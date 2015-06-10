from django import forms
from carros.models import Marca


class AgregarMarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ["nombre"]