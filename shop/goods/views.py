from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *


class ProductView(View):
    template = 'product.html'

    def get(self, request):
        # item = Goods.objects.get(slug=request.GET.get('slug'))
        return render(request, self.template, context={})


class CatalogView(View):
    template = 'catalog.html'

    def get(self, request):
        cat_id = request.GET.get('cat_id', '')
        products = Products.objects.all()

        if cat_id:
            products = products.filter(cat__pk=cat_id)

        on_sale = request.GET.get('on_sale', '')
        order_by = request.GET.get('order_by', '')

        if on_sale:
            products = products.exclude(discount=0)

        if order_by and order_by != 'default':
            products = products.order_by(order_by)

        return render(request, self.template, context={'products': products})
