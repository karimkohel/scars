from ultralytics import YOLO


model = YOLO("yolov8m-cls.pt")

if __name__ == "__main__":
    results = model.train(data="dataset/", epochs=20, amp=False, device="cpu")