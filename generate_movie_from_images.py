import cv2
import os

def generate_video():
    image_folder = "G:\Meine Ablage\EscapeFromTheDevilsEye\Renders"#os.path.join(os.getcwd(), 'game','images' )

    video_name = "G:\Meine Ablage\EscapeFromTheDevilsEye\Renders\intro_bathroom_spitroast00000.avi" #'./game/images/anim_hardong_2_shower.avi'
    images = [
        'intro_bathroom_spitroast00000.png',
        'intro_bathroom_spitroast00001.png',
        'intro_bathroom_spitroast00002.png',
        'intro_bathroom_spitroast00003.png',
        'intro_bathroom_spitroast00004.png',
        'intro_bathroom_spitroast00005.png',
        'intro_bathroom_spitroast00006.png',
        'intro_bathroom_spitroast00007.png',
        'intro_bathroom_spitroast00008.png',
        'intro_bathroom_spitroast00009.png',
        'intro_bathroom_spitroast00010.png',
        'intro_bathroom_spitroast00011.png',
        'intro_bathroom_spitroast00012.png',
        'intro_bathroom_spitroast00013.png',
        'intro_bathroom_spitroast00014.png',
        'intro_bathroom_spitroast00015.png',
        'intro_bathroom_spitroast00016.png',
        'intro_bathroom_spitroast00017.png',
        'intro_bathroom_spitroast00018.png',
        'intro_bathroom_spitroast00019.png',
        'intro_bathroom_spitroast00020.png',
        'intro_bathroom_spitroast00021.png',
        'intro_bathroom_spitroast00022.png',
        'intro_bathroom_spitroast00023.png',
        'intro_bathroom_spitroast00024.png',
        'intro_bathroom_spitroast00025.png',
        'intro_bathroom_spitroast00026.png',
        'intro_bathroom_spitroast00027.png',
        'intro_bathroom_spitroast00028.png',
        'intro_bathroom_spitroast00029.png',
        'intro_bathroom_spitroast00030.png',
        'intro_bathroom_spitroast00031.png',
        'intro_bathroom_spitroast00032.png',
        'intro_bathroom_spitroast00033.png',
        'intro_bathroom_spitroast00034.png',
        'intro_bathroom_spitroast00035.png',
        'intro_bathroom_spitroast00036.png',
        'intro_bathroom_spitroast00037.png',
        'intro_bathroom_spitroast00038.png',
        'intro_bathroom_spitroast00039.png',
    ]

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 30, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated


if __name__ == '__main__':
    generate_video()