from .backend import Backend
import numpy as np
from PIL import Image


class UploadedPicture(Backend):

    def __init__(self):
        Backend.__init__(self)
        self.picture = None
        self.set_image(Image.open("detection/static/images/sample.jpg"))

    def get_image_frame(self):
        return self.picture.copy()

    def set_image(self, image_data):
        width, height = image_data.size
        factor = 640 / width
        resized_content = image_data.resize((int(width * factor), int(height * factor)))
        self.picture = np.asarray(resized_content)

    def __del__(self):
        pass


picture_instance = UploadedPicture()
