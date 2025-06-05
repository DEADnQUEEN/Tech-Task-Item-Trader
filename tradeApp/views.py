from django.shortcuts import render, redirect, reverse
from django import http
from tradeApp import models, constraints


def home_page(request: http.HttpRequest) -> http.HttpResponse:
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect(reverse('register'))

    return redirect(reverse('show_offers'))


def show_items(request: http.HttpRequest, page: int = None) -> http.HttpResponse:
    if not page:
        page = 0

    items_count = models.Ad.objects.count()
    from_item = page * constraints.OBJECTS_PER_PAGE

    if from_item > items_count:
        raise http.Http404

    to_item = (page + 1) * constraints.OBJECTS_PER_PAGE
    ad_items = models.Ad.objects.all()
    if to_item > items_count:
        ad_items = ad_items[from_item:]
    else:
        ad_items = ad_items[from_item:to_item]

    return render(
        request,
        'pages/show trades.html',
        {
            'offers': ad_items
        }
    )
