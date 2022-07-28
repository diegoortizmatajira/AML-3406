from .backend import Backend
import numpy as np
from PIL import Image


class UploadedPicture(Backend):

    def __init__(self):
        Backend.__init__(self)
        image_data = Image.open("detection/static/images/sample.jpg")
        self.set_image(image_data)

    def get_image_frame(self):
        return self.picture

    def set_image(self, image_data):
        width, height = image_data.size
        factor = 640 / width
        resized_content = image_data.resize((int(width * factor), int(height * factor)))
        self.picture = np.asarray(resized_content)

    def __del__(self):
        pass


instance = UploadedPicture()
