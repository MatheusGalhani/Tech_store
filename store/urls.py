from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Login),
    url(r'^login/$', views.Login),
    url(r'^logout/(?P<id>[0-9]+)/$', views.Logout),
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
    url(r'^compras_realizadas/(?P<id>[0-9]+)/$', views.Historico),
    url(r'^sobre/$', views.Sobre),
    url(r'^suporte/$', views.Suporte),
    url(r'^compraindisponivel/$', views.CompraIndisponivel),
    url(r'^add_more/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.Add),
    url(r'^minus_more/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$', views.Minus),
]

handler404 = 'views.error404'