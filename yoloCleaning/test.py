import cv2
from ultralytics import YOLO
import torch


# img = "data/carFrontsProject/images/00aa9b3c-cffd-4da0-b920-ea8d5370168e_a3b4f332-81ec-4572-86c9-9994cc1b347b.jpeg"
img = "data/carFrontsProject/images/00aa9b3c-cffd-4da0-b920-ea8d5370168e_af63c2b9-e541-40c4-8db9-7c7539cdd085.jpeg"

# model = YOLO("yoloCleaning/runs/detect/train/weights/best.pt")
model = YOLO("yolov8s.pt")
results = model.predict(source=img, show=True, save=True)
print("________________________________________________________________________")

for result in results:
    bboxes = result.boxes.xyxy
    print(bboxes)