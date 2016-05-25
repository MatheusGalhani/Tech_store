from django.shortcuts import render, get_object_or_404
from .models import Produto, Carrinho, Contato
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CarrinhoForm
from django.contrib.auth.models import User
from random import choice
# Create your views here.
#return render(request, "store/error_page_404.html", {})
def LoginInvalido(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponseRedirect('/login_error/')
        else:
            return HttpResponseRedirect('/login_error/')

    return render(request, "store/login_invalid.html", {})

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
                #usuario nao ativo...
                return HttpResponseRedirect('/login_error/')
        else:
            return HttpResponseRedirect('/login_error/')

    products = Produto.objects.order_by('id_produto') 
    paginator = Paginator(products, 16)  #lista 16 produtos
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    paginas = [1 * str(i) for i in range(1,paginator.num_pages+1)]   
    return render(request, "store/post_list.html", {'posts': posts, 'redirect_to': next, 'paginas': paginas})

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
    products = Produto.objects.order_by('id_produto') 
    paginator = Paginator(products, 16)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    paginas = [1 * str(i) for i in range(1,paginator.num_pages+1)]   
    return render(request, "store/store.html", {'posts': posts, 'paginas': paginas})

def Product(request, pk):
    post = get_object_or_404(Produto, pk=pk)
    return render(request, 'store/product.html', {'post': post})

@login_required
def Buy(request, pk):
    #add funionalidades carrinho
    posts = Produto.objects.order_by('id_produto')
    return render(request, "store/cart.html", {'posts': posts})

def Reset(request):
    aux = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    senha = ''
    for s in range(15):
        senha += choice(aux)
    if request.method == "POST":
        email = request.POST['email']
        contato = Contato.objects.filter(email_contato=email)
        usuario = User.objects.filter(username = contato[0].author_usuario)
        usuario[0].set_password(senha)
        usuario[0].save()
        msg = 'Sua nova senha é '+ senha
        send_mail('Tech Store - RESET DE SENHA', msg, 'matheusgalhani@gmail.com', [email], fail_silently=False)
        return HttpResponseRedirect('/')
    return render(request, "store/reset_password.html", {})

def custom_404(request):
    return render(request, 'store/error_page_404.html', {})

def Categories(request, categoria):
    nome = categoria
    products = Produto.objects.filter(categoria_produto = nome)
    paginator = Paginator(products, 16)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    paginas = [1 * str(i) for i in range(1,paginator.num_pages+1)]   
    return render(request, "store/store.html", {'posts': posts, 'paginas': paginas})