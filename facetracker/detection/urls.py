from operator import index
from django.urls import path
from . import views

urlpatterns = [
    #display both cameras
    path('', views.index, name='index'),
    #access the laptop camera
    path('camera', views.camera, name='camera'),
    path('picture', views.picture, name='picture'),
    path('camera_endpoint', views.camera_endpoint, name='camera_endpoint'),
    path('picture_endpoint', views.picture_endpoint, name='picture_endpoint'),
]
