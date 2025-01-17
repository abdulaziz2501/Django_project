from django.urls import path
from .views import *


urlpatterns=[
    path('', customer_form, name="customer_form"),
    # path('list/', customer_list, name="customer_lists"),
]