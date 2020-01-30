from django.shortcuts import render
from django.core.paginator import Paginator
from pages.models import Detail
from django.db.models import Q


def shop(request):
    shop = Detail.objects.all()
    paginator = Paginator(shop, 6)
    page = request.GET.get('page')
    paged_shop = paginator.get_page(page)
    context = {
        'shop': paged_shop
    }
    return render(request, 'shop.html', context)

def search(request):
    queryset_list = Detail.objects.all()

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(title__icontains=keywords)
            )
    context = {
        'shop': queryset_list
    }
    return render(request, 'search.html', context)
