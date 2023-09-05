import requests
import io
from PIL import Image
import logging
import datetime
import os


class Handler():
    def __init__(self, dataDir: str) -> None:
        self.dataDir = dataDir
        logging.basicConfig(
            filename=dataDir+'.log',
            level=logging.DEBUG,
            format="%(asctime)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
        )
        self.logger = logging.getLogger()

        if not os.path.exists(dataDir):
            os.mkdir(dataDir)


    def download_image(self, src: str, fileName: str) -> None:
        try:
            webImage = requests.get(src).content
            imageData = io.BytesIO(webImage)
            image = Image.open(imageData)
            
            img_path = self.dataDir + '/' + fileName  + '.jpeg'

            with open(img_path, 'wb') as f:
                image.save(f, "JPEG")
        except Exception as e:
            print(e)
            print("Skipping")

    def log(self, msg: str) -> None:
        self.logger.debug(msg)