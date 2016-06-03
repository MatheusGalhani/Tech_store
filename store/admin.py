from django.contrib import admin
from .models import Produto, Statu, Contato, Carrinho
from daterange_filter.filter import DateRangeFilter


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

class CarrinhoAdmin(admin.ModelAdmin):
    model = Carrinho
    list_display = ['id_compra','usuario_compra', 'produto_compra', 'id_status']
    list_filter = [('created_date',DateRangeFilter),'created_date', 'usuario_compra', 'id_status']
    search_fields = ['produto_compra']
    save_on_top = False
    readonly_fields = ['id_carrinho', 'id_compra', 'usuario_compra','qntd_produtos', 'created_date', 'produto_compra', 'preco_total', 'id_status']
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Statu, StatuAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)