from classifier.yolo import classify_image
from ui import run

print('Launching Classroom Diagnostic Application')
run()

result = classify_image("anything")
for face in result.faces:
    print(f'Result: {face.tag} with probability: {face.probability * 100}%')
