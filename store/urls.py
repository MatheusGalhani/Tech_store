from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
]
