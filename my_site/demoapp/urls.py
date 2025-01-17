from django.urls import path
from .views import *


urlpatterns=[
    path('', main, name="main"),
    # path('list/', customer_list, name="customer_lists"),
]