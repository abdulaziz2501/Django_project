from django.urls import path
from .views import *

urlpatterns= [
    path('Table_database/', Table_database, name='Menu'),
    path('Countries_all/', Countries_all, name='Countries'),
    path('Employee/', Employee_all, name='Employees'),
    path('Employee_limit1/', Employee_limit1, name='Employees'),
    path('Employee_limit2/', Employee_limit2, name='Employees'),
    path('Employee_filter/', Employee_filter, name='Employee_filter'),
    path('Employee_like/', Employee_like, name='Employee_like'),
    path('Employee_between/', Employee_between, name='Employee_between'),
    path('Employee_and/', Employee_and, name='Employee_and'),
    path('Employee_in/', Employee_in, name='Employee_in'),
    path('Countries_count/', Countries_count, name='Countries counts'),
]