from django.urls import path
from .views import *
urlpatterns = [
    path('', marketing_func, name='items_page'),
    path('item/<str:slug>/', item_details, name = 'item_detail_urls'),
    path('homepage/', home_func, name='home_page'),
    path('registration/', register_func, name='reg_page'),

    path('category_page/', category_func, name='categ_site_n'),
    path('category_details/<str:slug>/', cat_detail_func, name='categ_detal_n')
]
