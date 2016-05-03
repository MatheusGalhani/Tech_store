from django.contrib import admin
from .models import Produto
from .models import Contato

class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    #list_display mostra nome do campo na coluna
    list_display = ['id_produto','nome_produto','preco_produto']
    list_filter = ['categoria_produto', 'nome_produto']
    search_fields = ['nome_produto']
    save_on_top = False

admin.site.register(Produto, ProdutoAdmin)

class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    #list_display mostra nome do campo na coluna
    list_display = ['id_contato','contato_nome','contato_email','cpf_contato']
    list_filter = ['contato_email','cpf_contato']
    search_fields = ['contato_nome']
    save_on_top = False

# Register your models here.
admin.site.register(Contato, ContatoAdmin)
