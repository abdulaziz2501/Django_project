from django.http import HttpResponse

def my_books(request):
    html = """
        <p> my books </p>
        <a href="back/"> books</a>

        """
    return HttpResponse(html)

def back(request):
    html="""
    <p> kitoblar </p>
    <a href="../"> ortga</a>
    
    """

    return HttpResponse(html)
