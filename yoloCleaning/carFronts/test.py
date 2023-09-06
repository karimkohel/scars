import cv2
from ultralytics import YOLO
import torch


# img = "data/carFrontsProject/images/00aa9b3c-cffd-4da0-b920-ea8d5370168e_a3b4f332-81ec-4572-86c9-9994cc1b347b.jpeg"
img = "data/LandRover_RangeRover_velar/a2a264fb-e6b5-4c58-8900-73816d857ca5_2cb11c82-297f-409f-baee-e40379515a72.jpeg"

# model = YOLO("yoloCleaning/runs/detect/train/weights/best.pt")
model = YOLO("yoloCleaning/best.pt")
results = model.predict(source=img, show=True, save=True, conf=0.8)
print("________________________________________________________________________")

print(results)