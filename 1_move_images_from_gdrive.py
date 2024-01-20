import os
import shutil

path_to_images_folder = "G:\Meine Ablage\EllenVague\images"

for file in os.listdir(path_to_images_folder):
    if file.endswith(".png"):
        shutil.move(os.path.join(path_to_images_folder, file),os.path.join(os.getcwd(), "game","images",file))