import requests
from PIL import Image
import io, os, logging


class Handler():
    def __init__(self, dataDir: str) -> None:
        self.dataDir = "data/" + dataDir
        logging.basicConfig(
            filename=dataDir+'.log',
            level=logging.DEBUG,
            format="%(asctime)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
        )
        self.logger = logging.getLogger()

        if os.path.exists(self.dataDir):
            self.legacyImages = os.listdir(self.dataDir)
        else:
            self.legacyImages = []
            os.mkdir(self.dataDir)


    def download_image(self, src: str, fileName: str) -> None:
        img_file_name = fileName  + '.jpeg'
        img_path = self.dataDir + '/' + img_file_name

        # check if image is already downloaded and exit if present
        if img_file_name in self.legacyImages:
            self.legacyImages.remove(img_file_name)
            print("found image locally, aborting!")
            return

        # try downloading
        try:
            webImage = requests.get(src).content
            imageData = io.BytesIO(webImage)
            image = Image.open(imageData)
            

            with open(img_path, 'wb') as f:
                image.save(f, "JPEG")
        except Exception as e:
            print(e)
            print("Skipping")

    def log(self, msg: str) -> None:
        self.logger.debug(msg)