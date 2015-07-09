from django.shortcuts import render
from xin.models import XinCar
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.db.models import Q


def latest_xin(request):
    xin_list = XinCar.objects.order_by("-id")
    page_size = 20
    after_range_num = 5
    before_range_num = 4
    paginator = Paginator(xin_list, page_size)
    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
        print page

    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        posts = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + before_range_num]
    return render(request, 'xin.html', {'xin_list': posts, 'page_range': page_range})


def search(request):
    query = request.GET.get('q', '')
    page_size = 20
    after_range_num = 5
    before_range_num = 4
    if query:
        qset = (
            Q(name__icontains=query)|
            Q(city__icontains=query)|
            Q(price__icontains=query)|
            Q(licensed_time__icontains=query)|
            Q(mile__icontains=query)
            )
        results = XinCar.objects.filter(qset).distinct()

    else:
        results = []
    return render(request, 'search.html', {'results': results, "query": query})
