from django.shortcuts import render
from .models import UploadImage
from .forms import UploadImageForm

def upload_image(request):
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadImageForm()

    images = UploadImage.objects.all()
    return render(request, "upload.html", {"form": form, "images": images})