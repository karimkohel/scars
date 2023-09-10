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


dataDir = 'data/LandRover_discovery/'

if __name__ == "__main__":
    # remove duplicates from raw scrapped data
    remove_duplicates(dataDir+"raw/")

    # use yolo obj detection to crop out images of cars and trucks
    crop_cars(dataDir)
    # remove any unwanted generated folders
    clean_slate(dataDir)

    # use custom trained yolo classification to get only the images we approve of
    classify_cars(dataDir)

    # remove duplicates from the filtered out images once again for good luck
    remove_duplicates(dataDir+"final_car_accepted/")
    remove_duplicates(dataDir+"final_truck_accepted/")
    
    print("Done for: ", dataDir)