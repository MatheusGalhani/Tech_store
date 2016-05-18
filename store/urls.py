from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Login),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^product/(?P<pk>[0-9]+)/', views.Product),
    url(r'^add_to_car/$', views.Buy),
    url(r'^reset_password/$', views.Reset),
    url(r'^search/$', views.Search),
    url(r'^cameras/$', views.cameras),
    url(r'^desktop/$', views.desktop),
    url(r'^hardware/$', views.hardware),
    url(r'^impressora/$', views.impressora),
    url(r'^notebook/$', views.notebook),
    url(r'^perifericos/$', views.perifericos),
    url(r'^redes/$', views.redes),
    url(r'^smartphone/$', views.smartphone),
    url(r'^software/$', views.software),
    url(r'^tablet/$', views.tablet),
    url(r'^televisao/$', views.televisao),
]

handler404 = 'views.custom_404'