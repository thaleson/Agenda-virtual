from django.contrib import admin

from .models import Categoria,Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display=('nome','sobrenome','telefone','email','data_criaçao','categoria', 'mostrar')
    list_display_links=('nome','sobrenome')
    # list_filter=('nome','sobrenome')
    list_per_page=10
    search_fields=('nome','sobrenome','telefone')
    list_editable= ('telefone','mostrar')
    
    
admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)