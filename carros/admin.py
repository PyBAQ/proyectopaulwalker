from django.contrib import admin

from .models import Carro, Marca


class CarrosAdmin(admin.ModelAdmin):
    fields = ['nombre', 'marca']
    list_display = ('nombre', 'marca')
    list_filter = ['marca']

class MarcaAdmin(admin.ModelAdmin):
	list_filter = ['nombre']

admin.site.register(Carro, CarrosAdmin)
admin.site.register(Marca, MarcaAdmin)