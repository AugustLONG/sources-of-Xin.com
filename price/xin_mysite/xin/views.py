from django.shortcuts import render
from xin.models import XinCar


def latest_xin(request):
    xin_list = XinCar.objects.order_by("-id")
    return render(request, 'xin.html', {'xin_list': xin_list})
