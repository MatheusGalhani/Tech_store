from django.shortcuts import render
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from tech_store import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
#def post_list(request):
#	posts = Produto.objects.order_by('id_produto')
#	return render(request, 'store/post_list.html', {'posts': posts})

def Login(request):
    posts = Produto.objects.order_by('id_produto')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                posts = Produto.objects.order_by('id_produto')
                return render(request, 'store/store.html', {'posts': posts})
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "store/post_list.html", {'posts': posts})

#def Login(request):
#    if request.method == "POST":
#       if 'username' in request.POST:
#          username = request.POST['username']
#         password = request.POST['password']
#        user = authenticate(username=username, password=password)
#       if user is not None:
#          if user.is_active:
#             login(request, user)
#            posts = Produto.objects.order_by('id_produto')
#           return render(request, 'store/store.html', {'posts': posts},  RequestContext(request))
#      else:
#         return HttpResponse("Inactive user.")
#            else:
#               return HttpResponseRedirect(settings.LOGIN_URL)
#  else:
#     return render(request, 'store/post_list.html', {},  RequestContext(request))

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
	posts = Produto.objects.order_by('id_produto')
	return render(request, 'store/store.html', {'posts': posts})