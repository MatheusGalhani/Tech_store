from django.contrib import admin
from .models import Produto
from .models import Contato

class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    #list_display mostra nome do campo na coluna
    list_display = ['id_produto','nome_produto','preco_produto']
    list_filter = ['nome_produto']
    search_fields = ['nome_produto']
    save_on_top = False

class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    #list_display mostra nome do campo na coluna
    list_display = ['id_contato','nome','email','cpf']
    list_filter = ['cpf']
    search_fields = ['nome']
    save_on_top = False

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contato, ContatoAdmin)
