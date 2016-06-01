from django.contrib import admin
from .models import Produto, Statu, Contato, Carrinho

class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    #list_display mostra nome do campo na coluna
    list_display = ['id_produto','nome_produto','preco_produto']
    list_filter = ['categoria_produto', 'nome_produto']
    search_fields = ['nome_produto']
    save_on_top = False

class StatuAdmin(admin.ModelAdmin):
    model = Statu
    #list_display mostra nome do campo na coluna
    list_display = ['id_status','status_info']
    list_filter = ['status_info']
    search_fields = ['status_info']
    save_on_top = False

class ContatoAdmin(admin.ModelAdmin):
	model = Contato
	list_display = ['id_contato','nome_completo', 'author_usuario', 'cpf_contato', 'email_contato']
	list_filter = ['author_usuario', 'cpf_contato', 'email_contato']
	search_fields = ['nome_completo']
	save_on_top = False

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Statu, StatuAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Carrinho)