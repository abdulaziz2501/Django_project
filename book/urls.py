from django.urls import path
from .views import my_books, back


urlpatterns=[
    path('', my_books, name='books'),
    path('back/', back, name='ortga')
]
