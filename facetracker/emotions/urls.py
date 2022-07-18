from operator import index
from django.urls import path
from . import views

urlpatterns = [
    #display both cameras
    path('', views.index, name='index'),
    #access the laptop camera
    path('get_emotions', views.get_emotions, name='get_emotions'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('results', views.results, name='results'),
]
