from django.shortcuts import render, get_object_or_404
from .models import Produto, Carrinho, Contato, Statu
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CarrinhoForm
from django.contrib.auth.models import User
from random import choice
from datetime import datetime
from django.conf.urls import handler404

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
                if user.is_staff:
                    return HttpResponseRedirect('/admin')
                else:
                    return HttpResponseRedirect(next)
            else:
                return render(request, "store/login_invalid.html", {'erro':2})
        else:
            return render(request, "store/login_invalid.html", {'erro':1})

    products = Produto.objects.filter(produto_indisponivel = False).order_by('id_produto') 
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
        posts = Produto.objects.filter(nome_produto__contains = search, produto_indisponivel = False)
        return render(request, "store/search.html", {'posts': posts})

    posts = Produto.objects.order_by('id_produto')
    return render(request, "store/search.html", {'posts': posts})

def Logout(request, id):   
    logout(request)
    cart = Carrinho.objects.filter(id_status=2, usuario_compra=id)
    for x in cart:
        x.id_status = Statu.objects.get(id_status=3)
        produto = Produto.objects.get(nome_produto = x.produto_compra)
        produto.qntd_produto = Produto.objects.get(nome_produto = x.produto_compra).qntd_produto + x.qntd_produtos
        produto.save()
        x.save()
    return HttpResponseRedirect('/')

@login_required
def Home(request):
    products = Produto.objects.filter(produto_indisponivel = False).order_by('id_produto') 
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
def Buy(request, pk, id):
    #add funionalidades carrinho
    if request.method == "POST":
        produto = get_object_or_404(Produto, pk=pk)
        produto.qntd_produto = Produto.objects.get(pk=pk).qntd_produto - 1
        produto.save()
        cart = Carrinho.objects.filter(id_status=2, usuario_compra=id)
        produto_existente = False
        form = CarrinhoForm()
        carrinho = form.save(commit=False)
        user = User.objects.get(id=id)
        if user.is_staff:
            return HttpResponseRedirect('/admin')
        else:
            if cart:
                numero_pedido = cart[0].id_compra
            else:
                numero_pedido = "".join([d for d in str(str(datetime.now())) if d.isdigit()])
                numero_pedido = str(id)+""+ numero_pedido
            for x in cart:
                if x.produto_compra == get_object_or_404(Produto, pk=pk):
                    produto_existente = True
            if produto_existente:
                cart = Carrinho.objects.filter(id_status=2, usuario_compra=id, produto_compra = produto)
                for x in cart:
                    x.qntd_produtos = (Carrinho.objects.get(id_carrinho = x.id_carrinho).qntd_produtos)+1
                    x.save()
                    x.preco_total = produto.preco_produto * (Carrinho.objects.get(id_carrinho = x.id_carrinho).qntd_produtos) 
                    x.save()
            else:
                carrinho.usuario_compra = user
                carrinho.qntd_produtos = 1
                carrinho.produto_compra = produto
                carrinho.preco_total = produto.preco_produto * carrinho.qntd_produtos 
                carrinho.id_status = get_object_or_404(Statu, pk=2)
                carrinho.id_compra = numero_pedido
                carrinho.save()
            return HttpResponseRedirect('/carrinho/%s/'%id)
    return render(request, "store/cart.html", {})

@login_required
def Historico(request, id):
    cart = Carrinho.objects.filter(usuario_compra=id)
    user = User.objects.get(id=id)
    if user.is_staff:
        return HttpResponseRedirect('/admin')
    else:
        mylist = []
        for x in cart:
            mylist.append(x.produto_compra)
        listapk = []
        for x in mylist:
            id = Produto.objects.filter(nome_produto__contains = x)
            listapk.append(id[0].id_produto)
        posts = Produto.objects.filter(id_produto__in = listapk)
        return render(request, "store/historico.html", {'posts': posts, 'cart':cart})

@login_required
def ExibicaoCarrinho(request, id):
    user = User.objects.get(id=id)
    if user.is_staff:
        return HttpResponseRedirect('/admin')
    else:
        cart = Carrinho.objects.filter(id_status=2, usuario_compra=id)
        mylist = []
        subtotal = 0
        for x in cart:
            mylist.append(x.produto_compra)
            subtotal += x.preco_total
        total = subtotal + 12
        listapk = []
        for x in mylist:
            id = Produto.objects.filter(nome_produto__contains = x)
            listapk.append(id[0].id_produto)
        posts = Produto.objects.filter(id_produto__in = listapk)
        return render(request, "store/cart.html", {'posts': posts, 'cart':cart, 'subtotal': subtotal, 'total': total})

@login_required
def CancelaCompra(request, pk, id):
    user = User.objects.get(id=id)
    if user.is_staff:
        return HttpResponseRedirect('/admin')
    else:
        produto = get_object_or_404(Produto, pk=pk)
        cart = Carrinho.objects.get(id_status=2, usuario_compra=id, produto_compra = produto)
        cart.id_status = Statu.objects.get(id_status=3)
        produto.qntd_produto = Produto.objects.get(pk=pk).qntd_produto + cart.qntd_produtos
        produto.save()
        cart.save()
        numero_pedido = "".join([d for d in str(str(datetime.now())) if d.isdigit()])
        numero_pedido = str(id)+""+ numero_pedido
        carrinho = Carrinho.objects.filter(id_status=2, usuario_compra=id)
        for x in carrinho:
            x.id_compra = numero_pedido
            x.save()
        return HttpResponseRedirect('/carrinho/%s/'%id)

@login_required
def FinalizaCompra(request, id):
    user = User.objects.get(id=id)
    if user.is_staff:
        return HttpResponseRedirect('/admin')
    else:
        cart = Carrinho.objects.filter(id_status=2, usuario_compra=id)
        for x in cart:
            x.id_status = Statu.objects.get(id_status=1)
            x.save()
        return render(request, "store/compra_realizada.html", {})

def Reset(request):
    aux = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    senha = ''
    for s in range(12):
        senha += choice(aux)
    if request.method == "POST":
        try:
            email = request.POST['email']
            contato = Contato.objects.filter(email_contato=email)
            usuario = User.objects.filter(username = contato[0].author_usuario)
            user = User.objects.get(id = usuario[0].id)
            user.set_password(senha)
            user.is_active=False
            user.save()
            msg = 'Sua nova senha é '+ senha + ' . Para alterar sua senha e ativar seu usuario, acesse: http://techstore.pythonanywhere.com/change_password/' #http://techstore.pythonanywhere.com/
            send_mail('Tech Store - RESET DE SENHA', msg, 'matheusgalhani@gmail.com', [email], fail_silently=False)
            return HttpResponseRedirect('/')
        except:
            return render(request, "store/reset_password.html", {'erro':1})
    return render(request, "store/reset_password.html", {'erro':0})

def Change(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['newsenha']
        oldsenha = request.POST['oldsenha']
        contato = Contato.objects.filter(email_contato=email)
        usuario = User.objects.filter(username = contato[0].author_usuario)
        user = User.objects.get(id = usuario[0].id)
        if user.check_password(oldsenha):
            user.set_password(senha)
            user.save()
            user.is_active=True
            user.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, "store/change_password.html", {'erro':1})
    return render(request, "store/change_password.html", {})

def error404(request):
    return render(request, 'store/error_page_404.html', {})

def Categories(request, categoria):
    nome = categoria
    products = Produto.objects.filter(categoria_produto = nome, produto_indisponivel = False)
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

def Sobre(request):
    return render(request, "store/sobre.html", {})

def Suporte(request):
    return render(request, "store/suporte.html", {})

def CompraIndisponivel(request):
    erro = 0
    products = Produto.objects.filter(produto_indisponivel = False).order_by('id_produto') 
    paginator = Paginator(products, 16)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    paginas = [1 * str(i) for i in range(1,paginator.num_pages+1)]   
    return render(request, "store/post_list.html", {'posts': posts, 'paginas': paginas, 'erro': erro})
