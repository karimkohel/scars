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
    dataDir = dataDir + 'raw/'
    phasher = PHash()
    encodings = phasher.encode_images(image_dir=dataDir)
    duplicates = phasher.find_duplicates_to_remove(encoding_map=encodings, outfile="filtering/dedup/toberemoved.json")
    for duplicate in duplicates:
        try:
            os.remove(dataDir + duplicate)
        except Exception as e:
            print("Exception in dedup remove loop: ", e)
            print("Skipping image: ", duplicate)