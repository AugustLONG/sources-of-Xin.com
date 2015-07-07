from django.contrib import admin
from xin.models import XinCar


class XinAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'price', 'licensed_time', 'mile')
    search_fields = ['name', 'city', 'price', 'licensed_time', 'mile']
admin.site.register(XinCar, XinAdmin)
