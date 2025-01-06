from django.urls import path
from .views import *


urlpatterns=[
    path('', my_books, name='books'),
    path('Istiqlol_jallodlari/', Istiqlol_jallodlari, name='Istiqlol_jallodlari'),
    path('back/', back, name='ortga')
]
