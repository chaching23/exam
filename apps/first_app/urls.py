from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^success$',views.success),
    url(r'^show/(?P<show_id>\d+)$', views.show),

    url(r'^logout$',views.logout),
    url(r'^create$',views.create),
    url(r'^join/(?P<show_id>\d+)/$', views.join),
    url(r'^show/(?P<show_id>\d+)/remove$', views.remove),

    # url(r'^display$',views.display),
    # url(r'^create$',views.create),
    # url(r'^logout$',views.logout),
    # url(r'^show/(?P<show_id>\d+)$', views.show),
    # url(r'^show/(?P<show_id>\d+)/edit$', views.edit),
    # url(r'^show/(?P<show_id>\d+)/delete$', views.delete),
    # url(r'^update/(?P<show_id>\d+)$', views.update),
    # url(r'^join/(?P<show_id>\d+)/$', views.join),
    # url(r'^show/(?P<show_id>\d+)/remove$', views.remove),






]
