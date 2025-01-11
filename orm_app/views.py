from django.shortcuts import render
from .models import Countries
from django.http import HttpResponse

# Create your views here.
def Countries(request):
    countries= Countries.objects.all()
    # for c in countries:
    #     print(c)
    country_list =""
    for c in countries:
        country_list +=f"<li>{c}</li>"
    return HttpResponse(f"<ul>{country_list}</ul>")


