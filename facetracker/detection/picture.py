from .backend import Backend
import numpy as np
from PIL import Image


class UploadedPicture(Backend):

    def __init__(self):
        Backend.__init__(self)
        content = Image.open("detection/static/images/sample.jpg")
        self.picture = np.asarray(content)

    def get_image_frame(self):
        return self.picture

    def set_image(self, image):
        self.picture = image

    def __del__(self):
        pass


instance = UploadedPicture()
