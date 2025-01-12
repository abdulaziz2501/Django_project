from django.shortcuts import render

from .models import *
from django.http import HttpResponse

# Create your views here.
def Countries_all(request):
    countries= Countries.objects.all()
    # for c in countries:
    #     print(c)
    country_list =""
    for c in countries:
        country_list +=f"<li>{c}</li>"
    country_list+='<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")


def Employee_all(request):
    emp= Employees.objects.all()
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"

    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")

def Employee_limit1(request):
    emp= Employees.objects.all()[:10]
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")

def Employee_limit2(request):
    emp= Employees.objects.all()[5:15]
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")


def Employee_filter(request):
    emp= Employees.objects.filter(employee_id=100)
    # Employees.objects.filter(age__gt=18)
    # Employees.objects.filter(age__gte=18)
    # Employees.objects.filter(age__lt=18)
    # Employees.objects.filter(age__lte=18)
    # Employees.objects.exclude(age=18)
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")


def Employee_between(request):
    emp= Employees.objects.filter(employee_id__range=(100, 110))
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")



def Employee_like(request):
    # WHERE name like '%A%';
    # WHERE name like binary '%A%';
    # WHERE name like 'A%';
    # WHERE name like binary 'A%';
    # WHERE name like '%A';
    # WHERE name like binary '%A';

    emp= Employees.objects.filter(first_name__icontains='A')
    # Employees.objects.filter(name__contains='A')
    # Employees.objects.filter(name__istartswith='A')
    # Employees.objects.filter(name__startswith='A')
    # Employees.objects.filter(name__iendswith='A')
    # Employees.objects.filter(name__endswith='A')
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")


def Employee_and(request):
    emp= Employees.objects.filter(employee_id=108, department_id=10)
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")


def Employee_in(request):
    emp= Employees.objects.filter(employee_id__in=[101, 102])
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.first_name}  {c.last_name}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")


def Location_not(request):
    emp= Locations.objects.exclude(country_id='US')
    country_list = ""
    for c in emp:
        country_list += f"<li>{c.city}</li>"
    country_list += '<a href="../">Ortga</a>'
    return HttpResponse(f"<ul>{country_list}</ul>")

def Countries_count(request):
    emp= Countries.objects.count()

    return HttpResponse(f"<ul>Countries counter - > {emp} <br> <a href='../'>Ortga</a></ul>")



# SELECT name
# FROM Book
# LEFT JOIN Publisher
# ON Book.publisher_id = Publisher.id
# WHERE Book.id=1;
#
#
# book = Book.objects.select_related('publisher').get(id=1)
# book.publisher.name



def Table_database(request):
    html = """
            <h1>Sample Database</h1>
            <ul>
                <li><a href="Countries_all">Countries_all</a></li>
                <li><a href="Employee_all">Employee_all</a></li>
                <li><a href="Employee_limit1">Employee_limit1</a></li>
                <li><a href="Employee_limit2">Employee_limit2</a></li>
                <li><a href="Employee_filter">Employee_filter</a></li>
                <li><a href="Employee_like">Employee_like</a></li>
                <li><a href="Employee_between">Employee_between</a></li>
                <li><a href="Employee_and">Employee_and</a></li>
                <li><a href="Employee_in">Employee_in</a></li>
                <li><a href="Location_not">Location_not</a></li>
                <li><a href="Countries_count">Countries_count</a></li>
            </ul>
        """
    return HttpResponse(html)