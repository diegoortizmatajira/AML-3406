from .. import *

def classify_image(image) -> Result:
    result = Result()
    result.add_face(DetectedFace(10, 10, 45, 50, 'Attentive', 0.98))
    return result
