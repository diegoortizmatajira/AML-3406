import torch
import cv2
import numpy as np


class Backend:

    def __init__(self):
        self.path_hubconfig = "./emotions/yolov5"
        self.path_weightfile = "emotions/yolov5/yolov5s.pt"  # or any custom trained model

        self.model = torch.hub.load(self.path_hubconfig,
                                    'custom',
                                    path=self.path_weightfile,
                                    source='local')

    def get_image_frame():
        raise NotImplementedError()

    #This function is used in views
    def get_frame(self):
        image = self.get_image_frame()
        results = self.model(image, size=640)
        #frame_flip = cv2.flip(results, 1)
        _, jpeg = cv2.imencode('.jpg', np.squeeze(results.render(0.5)))
        return jpeg.tobytes()
