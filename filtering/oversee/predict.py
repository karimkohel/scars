from ultralytics import YOLO
import shutil, os


def classify_cars(dataDir: str, classes: list[str] = ["car", "truck"]) -> None:
    """use Yolov8 trained classification model to oversee cars filtration and decide if a car works for us or not

    INPUT
    ---
    dataDir: required, the string path to the root directory of the car images, with the trailing slash

    classes: required, list containing the names of class folders to check in the data dir (default: ["car", "truck"])

    OUTPUT
    ---
    None
    """
    for classType in classes:
        try:
            os.makedirs(dataDir+f"final_{classType}_accepted")
        except FileExistsError:
            print(f"Files in final_{classType} already exist!")
            continue

    model = YOLO("filtering/oversee/best.pt")
    model.to('cuda')
    for classType in classes:
        results = model.predict(source=dataDir+'cropped/'+classType, stream=True)

        for result in results:
            probs = result.probs.top1
            if probs == 2: # code for car front
                shutil.copy(result.path, dataDir+f"final_{classType}_accepted/")
            # elif probs == 1:
            #     shutil.copy(result.path, dataDir+f"final_{classType}/rejected/")
            # else:
            #     print("Something went wrong when classifying: ", result.path, " with probs:", probs)



if __name__ == "__main__":
    # dataDir = "data/LandRove`r_discovery/"
    dataDir = "filtering/oversee/test1(3).jpg"

    model = YOLO("filtering/oversee/runs/classify/train4/weights/best.pt")
    model.to('cuda')
    results = model.predict(source=dataDir)


    for result in results:
        print(result.probs)