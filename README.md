# scars
scarping cars is a pipeline to fetch and process car image data for our private use in synapse

# Data Report
Final data is split into 2 folders, the final cleaned data of around 1000 for each car model, and the questionable set of data for each model that is images that are not 100% perfect and are taken from the front of the car but leaning towards one side more than the center



# requirements
requirements are gpu related and you should check your drivers and hardware version to cross reference with the torch version in the requirements file before installing, other than that it's all fair game and used under python 3.9 
> pip install -r requirements.txt

# Scraping
the scraping ordeal is broken down to whatever web scraping code you can write for your choice of website and a helper class that would help manage the data scraped

### Web scraping
The website chosen after careful consideration was [AutoScout24](https://www.autoscout24.com/) as it has over 3000+ entries for each Land Rover car model and multi-view images.

Brief walk over the code plan
- start the helper class and give it the dir to store the car model data
- enter the car make and model link with the page number in the url edited as a variable
- get the list of entries in the page and loop over each car
- enter the care detail page and find the urls for all the images
- get the image ID for each image and through a separate request from the server edit the url to request the correct image size
- hand the image src link to the handler to check if the image is a duplicate, then download convert and handle storage for each image, 
- keep looping over each car in the page
- keep looping for each page in the car model
- keep looping for each registration year for each car model

### Helper class
the helper class called ScrapingHandler handles the storing and downloading of all scrapped images, can be used with any scraping software as a generic helper for any website that would be chosen

```python
from helpers import ScrapingHandler

# check for dir or create it and load all existing image names if any to check for duplicates when downloading
handler = ScrapingHandler("data/LandRover_RangeRover_Vogue")

# check for image ID in the downloaded images and abort if present, download if not, handle errors and skip if corrupted image.
handler.download_image(SrcUrl)
```

# Filtering
The Filtering pipeline comprises of 4 steps:
- removing duplicates from raw scrapped images
- use yolov8 to filter out and crop images of cars and trucks in a different directory
- use yolov8 custom trained classifier to filter front facing car images
- use lenient hashing algo to remove duplicate cropped images

the system is broken into different directories housing different modules for each task and are combined in the main filtering.py script in the root of the filtering dir.

# Final manual steps
The final manual step was to check each folder of roughly 1000->2000 images and filter using Nezar's manual filtering tkinter tool to ensure quality at the final step.

