"""
- remove duplicates
- crop images (cars folder, trucks folder)
- classify in their (in their respective folders don't move)
    - copy accepted ones to new even more inside folder
"""
from imagededup.methods import PHash
import os
# first remove duplicate images, without insurance.

dataDir = 'data/LandRover_discovery/raw/'

if __name__ == "__main__":
    phasher = PHash()
    encodings = phasher.encode_images(image_dir=dataDir)
    duplicates = phasher.find_duplicates_to_remove(encoding_map=encodings)
