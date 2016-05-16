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
]

handler404 = 'views.custom_404'