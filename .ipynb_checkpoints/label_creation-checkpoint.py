import numpy as np
from PIL import Image
import os

pathogen_folder = os.path.join(os.getcwd(),"labels/pathogen")
prtri_folder = os.path.join(os.getcwd(),"labels/petri_dish")

output_folder = os.path.join(os.getcwd(),"labels/final_labels")




for filename in os.listdir(pathogen_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        pathogen_path = os.path.join(pathogen_folder, filename)
        prtri_path = os.path.join(prtri_folder, filename)

        # three type of classes
        bg_mask = np.array(Image.open(pathogen_path))   # background mask = 0
        pathogen_mask = np.array(Image.open(pathogen_path)) # pathogen_mask = 1
        prtri_mask = np.array(Image.open(prtri_path)) # prtri_mask = 2

        # initialize 0
        final_mask = np.zeros_like(bg_mask)

        final_mask[prtri_mask == 255] = 2
        final_mask[pathogen_mask == 255] = 1
        # print(final_mask[110])
        Image.fromarray(final_mask.astype(np.uint8)).save(os.path.join(output_folder, filename))



