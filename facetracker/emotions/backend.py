import torch
import cv2
import numpy as np
import base64
import random
from pprint import pprint


class Backend:

    def __init__(self):
        self.path_hubconfig = "./emotions/yolov5"
        # self.path_weightfile = "emotions/yolov5/yolov5s.pt"  # or any custom trained model
        self.path_weightfile = "emotions/best.pt"  # or any custom trained model

        self.model = torch.hub.load(self.path_hubconfig,
                                    'custom',
                                    path=self.path_weightfile,
                                    source='local')

    def get_image_frame():
        raise NotImplementedError()

    #This function is used in views
    def get_response(self):
        image = self.get_image_frame()
        results = self.model(image, size=640)
        _, jpeg = cv2.imencode('.jpg', np.squeeze(results.render(0.5)))
        bytes = jpeg.tobytes()
        return {
            "ImageBase64": base64.b64encode(bytes).decode("utf-8"),
            "ImageType": "image/jpeg;",
            "Detail": results.pandas().xyxy[0].to_json(orient="records")
        }
