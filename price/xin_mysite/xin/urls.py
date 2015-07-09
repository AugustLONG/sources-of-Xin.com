from django.conf.urls import patterns, url

from xin import views

urlpatterns = patterns(' ',
                                 url(r'^$', views.latest_xin, name='latest_xin'),
                                 url(r'^$', views.search, name='search'),
                                 )