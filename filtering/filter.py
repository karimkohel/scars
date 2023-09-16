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



if __name__ == "__main__":

    dataDir = [
        'data/LandRover_RangeRover_Vogue/'
    ]

    for carDir in dataDir:
        # remove duplicates from raw scrapped data
        #remove_duplicates(carDir+"raw/")

        # use yolo obj detection to crop out images of cars and trucks
        #crop_cars(carDir)
        # remove any unwanted generated folders
        #clean_slate(carDir)


        # use custom trained yolo classification to get only the images we approve of
        classify_cars(carDir)

        # remove duplicates from the filtered out images once again for good luck
        remove_duplicates(carDir+"final_car_accepted/")
        remove_duplicates(carDir+"final_truck_accepted/")

        print("Done for: ", carDir)