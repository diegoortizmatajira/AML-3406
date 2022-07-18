import cv2
from .backend import Backend


class VideoCamera(Backend):

    def __init__(self):
        Backend.__init__(self)
        self.video = cv2.VideoCapture(0)

    def get_image_frame(self):
        _, image = self.video.read()
        return image

    def __del__(self):
        self.video.release()
