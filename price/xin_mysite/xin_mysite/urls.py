from django.conf.urls import patterns, include, url
from django.contrib import admin
from xin import views


urlpatterns = patterns(' ',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xin/', include('xin.urls')),
    url(r'^search/$', views.search),
)
