from django.shortcuts import render
from django.http import JsonResponse
from . import camera as camera_module
from . import picture as picture_module
from . import picture_upload as picture_upload_module
from PIL import Image


# Create your views here.
#Display the 2 videos
def index(request):
    return render(request, 'home.html')


#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py


def camera(request):
    return render(request, 'camera.html')


def picture(request):
    return render(request, 'picture.html')


def camera_endpoint(_):
    return JsonResponse(camera_module.instance.get_response())


def picture_endpoint(_):
    return JsonResponse(picture_module.instance.get_response())


def picture_upload(request):
    if request.method == 'POST':
        form = picture_upload_module.PictureForm(request.POST, request.FILES)
        if form.is_valid():
            picture_data = Image.open(form.cleaned_data["picture"])
            picture_module.instance.set_image(picture_data)
    return render(request, 'picture.html')
