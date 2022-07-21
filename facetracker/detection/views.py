from django.shortcuts import render
from django.http import JsonResponse
from . import camera as camera_module , picture as picture_module


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
