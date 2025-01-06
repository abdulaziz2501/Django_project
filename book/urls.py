from django.urls import path
from views import my_books


urlpatterns=[
    path('', my_books, namme='books')
]
