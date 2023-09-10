from imagededup.methods import PHash
import os


def remove_duplicates(dataDir: str) -> None:
    """Remove duplicate images from a given directory

    INPUT
    ---
    dataDir: required, the string path to the root directory of the car images, with the trailing slash

    OUTPUT
    ---
    None
    """
    phasher = PHash()
    encodings = phasher.encode_images(image_dir=dataDir)
    duplicates = phasher.find_duplicates_to_remove(encoding_map=encodings)
    for duplicate in duplicates:
        try:
            os.remove(dataDir + duplicate)
        except Exception as e:
            print("Exception in dedup remove loop: ", e)
            print("Skipping image: ", duplicate)

if __name__ == '__main__':
    remove_duplicates("data/LandRover_defender/final_truck_accepted/")