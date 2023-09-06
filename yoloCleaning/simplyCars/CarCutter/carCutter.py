import os
from ultralytics import YOLO

"""

a small work in progress module that takes input a directory full of images and would then crop cars out of said images if detected above a certain confidence score

"""

class CarCutter():
    def __init__(self, dataDir: str, saveDir: str, conf: float) -> None:
        pass