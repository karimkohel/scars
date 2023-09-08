from ultralytics import YOLO
from numpy import argmax

# dataDir = "data/LandRover_discovery/"
dataDir = "r.jpg"

model = YOLO("filtering/best.pt")
model.to('cuda')
results = model.predict(source=dataDir)


for result in results:
    probs = result.probs.top1
    if probs == 0:
        print("image accepted")
    elif probs == 1:
        print("rejected")
    else:
        print(probs)