from django.urls import path
from .views import *

urlpatterns= [
    path('', orm_list, name='orm_list')
]