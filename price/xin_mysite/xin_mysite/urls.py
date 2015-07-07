from django.conf.urls import include, url
from django.contrib import admin
from xin import views as xin_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xin/', xin_views.latest_xin),
]
