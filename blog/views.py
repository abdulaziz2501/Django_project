from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_lists(request):
    html="""
    <p>blog</p>"""
    return HttpResponse(html)