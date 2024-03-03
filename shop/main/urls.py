from django.urls import path

from .views import *


app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]