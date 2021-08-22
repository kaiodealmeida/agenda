from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'mostrar')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email', 'id')
    list_editable = ('telefone', 'email', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
