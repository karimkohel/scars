"""
- remove duplicates
- crop images (cars folder, trucks folder)
- classify in their (in their respective folders don't move)
    - copy accepted ones to new even more inside folder

Note: must locate the car directory in dataDir for now but if successful, should loop over all cars    
"""
from dedup.dedup import remove_duplicates
from crop.cropper import crop_cars, clean_slate
from oversee.predict import classify_cars


dataDir = 'data/LandRover_defender/'

if __name__ == "__main__":
    # remove_duplicates(dataDir)
    # crop_cars(dataDir)
    # clean_slate(dataDir)
    classify_cars(dataDir)
    print("Done for: ", dataDir)