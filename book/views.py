from django.http import HttpResponse


def my_books(request):
    html="""
    <p> my books </p>
    <a href="book/"> books</a>
    
    """

    return HttpResponse(html)
