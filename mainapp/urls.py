from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('item/<pk>', item, name='item'),
    path('buy/<pk>', buy, name='buy')

]

