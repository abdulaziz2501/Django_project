from django.shortcuts import render
from .models import Countries

# Create your views here.
def orm_list(request):
    countries= Countries.objects.all()
    for c in countries:
        print(c)

