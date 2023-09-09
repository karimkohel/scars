from ultralytics import YOLO
import os, shutil


def crop_cars(dataDir: str) -> None:
    """use YOLOv8 to crop out car images from the raw set of data, will place the output images in folders cars and trucks in a subfolder called cropped

    INPUT
    ---
    dataDir: required, the string path to the root directory of the car images, with the trailing slash

    OUTPUT
    ---
    None
    """
    model = YOLO("filtering/crop/yolov8s.pt")
    model.to('cuda')
    results = model.predict(source=dataDir+"raw/", conf=0.7, stream=True)

    for result in results:
        for predictedClass in result.boxes.cls:
            if int(predictedClass) in [2, 7]: # cars and trucks
                result.save_crop(dataDir+"cropped/", result.path.split("/")[-1])

def clean_slate(dataDir: str, classes: list[str] = ["car", "truck"]) -> None:
    """remove any reminiscent yolov8 folders for unwanted cropped images

    INPUT
    ---
    dataDir: required, the string path to the root directory of the car images, with the trailing slash

    classes: required, list containing the names of class folders to check in the data dir (default: ["car", "truck"])

    OUTPUT
    ---
    None
    """
    croppedDirs = [filename for filename in os.listdir(dataDir+'cropped/') if os.path.isdir(os.path.join(dataDir+'cropped/',filename))]
    for folder in croppedDirs:
        if folder not  in classes:
            shutil.rmtree(dataDir+"cropped/"+folder)