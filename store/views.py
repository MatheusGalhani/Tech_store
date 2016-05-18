from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
#return render(request, "store/error_page_404.html", {})
def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return render(request, "store/login_invalid.html", {})
        else:
            return render(request, "store/login_invalid.html", {})

    posts = Produto.objects.order_by('id_produto')        
    return render(request, "store/post_list.html", {'posts': posts, 'redirect_to': next})

def Search(request):
    if request.method == "GET":
        search = request.GET['search']
        posts = Produto.objects.filter(nome_produto__contains = search)
        return render(request, "store/search.html", {'posts': posts})

    posts = Produto.objects.order_by('id_produto')
    return render(request, "store/search.html", {'posts': posts})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def Home(request):
    posts = Produto.objects.order_by('id_produto')
    return render(request, "store/store.html", {'posts': posts})

def Product(request, pk):
    post = get_object_or_404(Produto, pk=pk)
    return render(request, 'store/product.html', {'post': post})

def Buy(request):
    posts = Produto.objects.order_by('id_produto')
    return render(request, "store/store.html", {'posts': posts})

def Reset(request):
    #contatotechstore@hotmail.com
    return render(request, "store/reset_password.html", {})

def custom_404(request):
    return render(request, 'store/error_page_404.html', {})

def cameras(request):
    posts = Produto.objects.filter(categoria_produto = 'cameras')
    return render(request, "store/store.html", {'posts': posts})

def desktop(request):
    posts = Produto.objects.filter(categoria_produto = 'desktop')
    return render(request, "store/store.html", {'posts': posts})

def hardware(request):
    posts = Produto.objects.filter(categoria_produto = 'hardware')
    return render(request, "store/store.html", {'posts': posts})

def impressora(request):
    posts = Produto.objects.filter(categoria_produto = 'impressora')
    return render(request, "store/store.html", {'posts': posts})

def notebook(request):
    posts = Produto.objects.filter(categoria_produto = 'notebook')
    return render(request, "store/store.html", {'posts': posts})

def perifericos(request):
    posts = Produto.objects.filter(categoria_produto = 'perifericos')
    return render(request, "store/store.html", {'posts': posts})

def redes(request):
    posts = Produto.objects.filter(categoria_produto = 'redes')
    return render(request, "store/store.html", {'posts': posts})

def smartphone(request):
    posts = Produto.objects.filter(categoria_produto = 'smartphone')
    return render(request, "store/store.html", {'posts': posts})

def software(request):
    posts = Produto.objects.filter(categoria_produto = 'software')
    return render(request, "store/store.html", {'posts': posts})

def tablet(request):
    posts = Produto.objects.filter(categoria_produto = 'tablet')
    return render(request, "store/store.html", {'posts': posts})

def televisao(request):
    posts = Produto.objects.filter(categoria_produto = 'televisao')
    return render(request, "store/store.html", {'posts': posts})