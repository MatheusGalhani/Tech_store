from django.contrib import admin
from .models import Products

class ProdutoAdmin(admin.ModelAdmin):
    model = Products
    #list_display mostra nome do campo na coluna
    list_display = ['id_produto','nome_produto','preco_produto']
    list_filter = ['nome_produto']
    search_fields = ['nome_produto']
    save_on_top = False
# Register your models here.
admin.site.register(Products, ProdutoAdmin)
