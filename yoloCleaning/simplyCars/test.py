import os
from ultralytics import YOLO

dataDir = 'data/'

imgs = os.listdir(dataDir)
imgs = [dataDir+img for img in imgs]

model = YOLO("yolov8s.pt")
results = model.predict(source=imgs[0], conf=0.6)

print("___________________________________________________")
for result in results:
    result.save_crop("cleaned/", result.path.split("/")[-1])
    print(result.names[int(result.boxes.cls)])
