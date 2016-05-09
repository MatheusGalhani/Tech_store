from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    #list_display mostra nome do campo na coluna
    list_display = ['id_produto','nome_produto','preco_produto']
    list_filter = ['categoria_produto', 'nome_produto']
    search_fields = ['nome_produto']
    save_on_top = False

admin.site.register(Produto, ProdutoAdmin)

