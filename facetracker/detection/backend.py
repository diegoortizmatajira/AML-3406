import json
import torch
import cv2
import numpy as np
import base64
import pandas as pd


class Backend:

    def __init__(self):
        self.path_hubconfig = "./detection/yolov5"
        self.path_weightfile = "detection/best.pt"  # or any custom trained model

        self.model = torch.hub.load(self.path_hubconfig,
                                    'custom',
                                    path=self.path_weightfile,
                                    source='local')

    def get_image_frame():
        raise NotImplementedError()

    def process_dataframe(self, dataframe: pd.DataFrame):
        clean_df: pd.DataFrame = dataframe[['confidence', 'class', 'name']]
        results: dict = clean_df.to_dict('records')
        summary_df: pd.DataFrame = clean_df.groupby(
            ['class', 'name']).size().reset_index(name='count')
        summary = summary_df.to_dict('records')
        return json.dumps({'results': results, 'summary': summary})

    #This function is used in views
    def get_response(self):
        image = self.get_image_frame()
        print(type(image))
        if image is None :
            return {
                "ImageBase64": None,
                "ImageType": None,
                "Detail": {}
            }

        results = self.model(image, size=640)
        _, jpeg = cv2.imencode('.jpg', np.squeeze(results.render(0.5)))
        bytes = jpeg.tobytes()
        detail = self.process_dataframe(results.pandas().xyxy[0])
        return {
            "ImageBase64": base64.b64encode(bytes).decode("utf-8"),
            "ImageType": "image/jpeg;",
            "Detail": detail
        }
