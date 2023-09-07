from ultralytics import YOLO

dataDir = "data/LandRover_discovery/"
# dataDir = "data/"

model = YOLO("yolov8s.pt")
model.to('cuda')
results = model.predict(source=dataDir, conf=0.7, stream=True)


for result in results:
    for predictedClass in result.boxes.cls:
        if int(predictedClass) in [2, 7]:
            result.save_crop(dataDir+"cropped/", result.path.split("/")[-1])