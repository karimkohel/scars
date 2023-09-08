from ultralytics import YOLO


model = YOLO("yolov8m-cls.pt")

if __name__ == "__main__":
    results = model.train(data="filtering/dataset/", epochs=15, amp=False, device='cpu')
    # try batch=2 , might work