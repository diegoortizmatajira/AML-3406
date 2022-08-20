import torch
import cv2
import numpy as np
import base64
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
from io import BytesIO

path_hubconfig = "./detection/yolov5"
path_weightfile = "detection/best.pt"  # or any custom trained model
model = torch.hub.load(path_hubconfig,
                       'custom',
                       path=path_weightfile,
                       source='local')

LABELS = ['Attentive', 'Distracted', 'Sleepy']
COLORS= ['green', 'orange', 'blue', 'silver']

class Backend:

    def __init__(self):
        self.history_df = None
        self.initialize_history_df()

    def get_image_frame(self):
        raise NotImplementedError()

    def initialize_history_df(self):
        self.history_df = pd.DataFrame({
            'timestamp': [],
            'class': [],
            'name': [],
            'count': [],
        })

    def reset_history_df(self):
        self.history_df = self.history_df[0:0]

    def process_dataframe(self, dataframe: pd.DataFrame):
        now = datetime.now()
        clean_df: pd.DataFrame = dataframe[['confidence', 'class', 'name']]
        # creates a new summary dataframe by grouping and counting per class
        summary_df: pd.DataFrame = clean_df.groupby(
            ['class', 'name']).size().reset_index(name='count')
        added_rows = []
        if len(summary_df) == 0:
            added_rows.append({'confidence': 0, 'name': 'Unknown', 'count': 1})
            
        # adds zero count rows
        for label in LABELS:
            temp = summary_df[summary_df['name'] == label]
            if len(temp) == 0:
                added_rows.append({'confidence': 0, 'name': label, 'count': 0})
        temp_df = pd.DataFrame(added_rows)
        summary_df = pd.concat([summary_df, temp_df])

        # adds timestamp to the dataframe
        summary_df['timestamp'] = now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        # adds the current frame results to the history_df
        self.history_df = pd.concat([self.history_df, summary_df])

        # Generates the pie chart for the results
        fig = plt.figure(figsize=(8, 6))
        summary_df.groupby(['name']).sum().plot(kind='pie', y='count', colors= COLORS)
        fig.canvas.draw()
        bytes_io = BytesIO()
        plt.savefig(bytes_io)
        buf = bytes_io.getvalue()
        return self.buffer_to_base64(buf)

    def generate_historic_chart(self):
        if len(self.history_df) == 0:
            return None
        df = self.history_df.drop(['class'], axis=1)
        gdf = df.groupby(['timestamp', 'name']).sum('count')
        gdf = gdf['count'].unstack()
        # Normalize the values to sum 1.0
        gdf = gdf.divide(gdf.sum(axis=1), axis=0)
        fig = plt.figure(figsize=(8, 6))
        gdf.plot.area(stacked=True)
        fig.canvas.draw()
        bytes_io = BytesIO()
        plt.savefig(bytes_io)
        buf = bytes_io.getvalue()
        return self.buffer_to_base64(buf)

    def buffer_to_base64(self, bytes):
        return None if bytes == None else base64.b64encode(bytes).decode(
            "utf-8")

    #This function is used in views
    def get_response(self):
        image = self.get_image_frame()
        if image is None:
            return {"ImageBase64": None, "ImageType": None, "Detail": {}}

        results = model(image, size=640)
        _, jpeg = cv2.imencode('.jpg', np.squeeze(results.render(0.5)))

        # Gets the results to send to the frontend
        return {
            "ImageType": "image/jpeg;",
            "ImageBase64": self.buffer_to_base64(jpeg.tobytes()),
            "PieChartBase64": self.process_dataframe(results.pandas().xyxy[0]),
            "HistoricChartBase64": self.generate_historic_chart(),
        }
