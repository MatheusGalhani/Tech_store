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
    if request.method == "POST":
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        return HttpResponse(from_email)
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, "store/reset_password.html", {})
