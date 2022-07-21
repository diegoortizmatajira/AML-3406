from .backend import Backend


class UploadedPicture(Backend):

    def __init__(self):
        Backend.__init__(self)

    def get_image_frame(self):
        return None

    def __del__(self):
        pass

instance = UploadedPicture()
