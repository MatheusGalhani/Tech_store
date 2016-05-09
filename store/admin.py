from django.contrib import admin
from .models import Produto, Pagamento, Statu 

class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    #list_display mostra nome do campo na coluna
    list_display = ['id_produto','nome_produto','preco_produto']
    list_filter = ['categoria_produto', 'nome_produto']
    search_fields = ['nome_produto']
    save_on_top = False



class PagamentoAdmin(admin.ModelAdmin):
    model = Pagamento
    #list_display mostra nome do campo na coluna
    list_display = ['id_pagamento','tipo_pagamento']
    list_filter = ['tipo_pagamento']
    search_fields = ['tipo_pagamento']
    save_on_top = False



class StatuAdmin(admin.ModelAdmin):
    model = Statu
    #list_display mostra nome do campo na coluna
    list_display = ['id_status','status_info']
    list_filter = ['status_info']
    search_fields = ['status_info']
    save_on_top = False

admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Statu, StatuAdmin)