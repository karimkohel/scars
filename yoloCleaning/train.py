from ultralytics import YOLO


model = YOLO("yolov8m-cls.pt")
# model.to('cuda')
if __name__ == "__main__":
    results = model.train(data="dataset/", epochs=10)