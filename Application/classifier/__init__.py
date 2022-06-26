class DetectedFace:
    x: int
    y: int
    width: int
    height: int
    tag: str
    probability: float

    def __init__(self, x: int, y: int, width: int, height: int, tag: str,
                 probability: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tag = tag
        self.probability = probability


class Result:
    faces: list[DetectedFace]

    def __init__(self):
        self.faces = []

    def add_face(self, face: DetectedFace):
        self.faces.append(face)
