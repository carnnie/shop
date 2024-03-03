from django.urls import path

from .views import *


app_name = 'goods'

urlpatterns = [
    path('product/', ProductView.as_view(), name='product'),
    path('catalog/', CatalogView.as_view(), name='catalog')
]
