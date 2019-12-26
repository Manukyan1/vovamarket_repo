from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def marketing_func(request):
    items = ad_adding.objects.all()
    return render(request, 'marketapp/index.html', context = {'ads': items})


def item_details(request, slug):

    item = ad_adding.objects.get(slug__iexact=slug)
    return render(request, 'marketapp/item_detail_template.html', context={'ad_detail': item})

def home_func(request):
    return render(request, 'marketapp/hometemp.html')
#------------------------------------------------------------------------

def register_func(request):
    return render(request, 'marketapp/registertemplate.html')
#---------------------------------------------------------------------------

def category_func(request):
    categor_var = Tag.objects.all()
    return render(request, 'marketapp/catergory_list.html', context = {'cvar_key': categor_var})


def cat_detail_func(request, slug):
    var_for_slug = Tag.objects.all()
    detail_var = Tag.objects.get(slug__iexact=slug)
    return render(request, 'marketapp/category_detail.html', context={'c_detail': detail_var, 'c_havayi': var_for_slug})
