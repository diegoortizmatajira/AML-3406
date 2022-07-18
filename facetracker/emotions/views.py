from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.http import JsonResponse
from . import camera


# Create your views here.
#Display the 2 videos
def index(request):
    return render(request, 'EMOTIONS/home.html')


#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py
def get_emotions(request):
    return render(request, 'EMOTIONS/camera.html')


def results(request):
    return render(request, 'EMOTIONS/results.html')


def gen(camera):

    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


#Method for laptop camera
def video_feed(_):
    return StreamingHttpResponse(
        gen(camera.VideoCamera()),
        #video type
        content_type='multipart/x-mixed-replace; boundary=frame')


def camera_endpoint(_):
    return JsonResponse(camera.instance.get_response())
