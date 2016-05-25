from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Login),
    url(r'^login/$', views.Login),
    url(r'^login_error/$', views.LoginInvalido),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^product/(?P<pk>[0-9]+)/', views.Product),
    url(r'^add_to_car/(?P<pk>[0-9]+)/$', views.Buy),
    url(r'^reset_password/$', views.Reset),
    url(r'^search/$', views.Search),
    url(r'^categoria/(?P<categoria>\w+)/$', views.Categories),
]

handler404 = 'views.custom_404'