from django.shortcuts import render
from django.http import JsonResponse
from . import camera


# Create your views here.
#Display the 2 videos
def index(request):
    return render(request, 'home.html')


#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py
def get_emotions(request):
    return render(request, 'camera.html')


def results(request):
    return render(request, 'results.html')

def camera_endpoint(_):
    return JsonResponse(camera.instance.get_response())
