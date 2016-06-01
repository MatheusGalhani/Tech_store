from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Login),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^product/(?P<pk>[0-9]+)/', views.Product),
    url(r'^add_to_car/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.Buy),
    url(r'^reset_password/$', views.Reset),
    url(r'^change_password/$', views.Change),
    url(r'^search/$', views.Search),
    url(r'^categoria/(?P<categoria>\w+)/$', views.Categories),
    url(r'^carrinho/(?P<id>[0-9]+)/$', views.ExibicaoCarrinho),
    url(r'^cancela_pedido/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.CancelaCompra),
    url(r'^checkout/(?P<id>[0-9]+)/$', views.FinalizaCompra),
]

handler404 = 'views.custom_404'