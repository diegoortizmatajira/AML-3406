from imutils.video import VideoStream
import imutils
import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings

import torch



class VideoCamera(object):
    

    def __init__(self):
        self.path_hubconfig = "/Users/juliosanchez/Documents/LAMBTON/SEMESTER3/Saturday/facetracker/emotions/yolov5"
        self.path_weightfile = "emotions/yolov5/yolov5s.pt"  # or any custom trained model

        self.model = torch.hub.load(self.path_hubconfig, 'custom',
                            path=self.path_weightfile, source='local')
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()


    #This function is used in views
    def get_frame(self):

        success, image = self.video.read()
        results = self.model(image,size=640)
        #frame_flip = cv2.flip(results, 1)
        ret, jpeg = cv2.imencode('.jpg', np.squeeze(results.render(0.5)))
        return jpeg.tobytes()

