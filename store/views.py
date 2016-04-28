from django.shortcuts import render
from .models import Produto
# Create your views here.
def post_list(request):
	posts = Produto.objects.order_by('id_produto')
	return render(request, 'store/post_list.html', {'posts': posts})

