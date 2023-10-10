"""
The helper class module for simplifying web scrapping.

(this module should have included logging but i was too burnt out too add it, it was a simple logging class implementation away.)
"""

import requests
from PIL import Image
import io, os, logging



class ScrapingHandler():
    """Helper class that simplifies the scrapping process by handling directory, file downloads and file duplication
    """
    def __init__(self, dataDir: str) -> None:
        """
        INPUT
        ---
        dataDir: required, directory to place scraped data or compare new data being scraped with duplicates already downloaded
        """
        self.dataDir = dataDir

        if os.path.exists(self.dataDir):
            self.legacyImages = os.listdir(self.dataDir)
        else:
            self.legacyImages = []
            os.mkdir(self.dataDir)


    def download_image(self, src: str, fileName: str) -> None:
        """
        helper method that would download the requested image and place it in the appropriate place after checking if it's not already there.

        INPUT:
        ---
        src: required, source url for the image requested

        fileName: required, the unique file name for the file to be saved with and checked against already downloaded files
        """
        img_file_name = fileName  + '.jpeg'
        img_path = self.dataDir + '/' + img_file_name

        # check if image is already downloaded and exit if present
        if img_file_name in self.legacyImages:
            self.legacyImages.remove(img_file_name)
            print("found image locally, skipping!")
            return

        # try downloading
        try:
            webImage = requests.get(src).content
            imageData = io.BytesIO(webImage)
            image = Image.open(imageData)
            

            with open(img_path, 'wb') as f:
                image.save(f, "JPEG")
        except Exception as e:
            print("WARNING: image was not downloaded, aborting")
            print(e)
            print("---------------------------------------------------------")