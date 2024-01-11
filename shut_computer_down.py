import time
import os
# This tool is used to shut off my render machine if no new images are detected in my render folder for twenty minutes.
# Usual render times per image are 5-10 minutes, so this catches both crashes of the render program, as well as potential renders that are set up wrong and exceed that time frame.

path_to_images_folder = "G:\My Drive\EllenVague\images"
number_of_images = 0

def main():
    number_of_images = sum(len(files) for _, _, files in os.walk(path_to_images_folder))
    while True:
        time.sleep(10)
        #time.sleep(20*60)
        current_number_of_images = sum(len(files) for _, _, files in os.walk(path_to_images_folder))
        if number_of_images == current_number_of_images:
            print("Shutting down render machine")
            os.system("shutdown /s /t 20")
        else:
            number_of_images = current_number_of_images



if __name__ == '__main__':
    main()