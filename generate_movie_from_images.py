import cv2
import os

def generate_video():
    image_folder = os.path.join(os.getcwd(), 'game','images' )

    video_name = './game/images/anim_hardong_2_shower.avi'
    images = [
        'anim_hardong_2_shower00000.webp',
        'anim_hardong_2_shower00001.webp',
        'anim_hardong_2_shower00002.webp',
        'anim_hardong_2_shower00003.webp',
        'anim_hardong_2_shower00004.webp',
        'anim_hardong_2_shower00005.webp',
        'anim_hardong_2_shower00006.webp',
        'anim_hardong_2_shower00007.webp',
        'anim_hardong_2_shower00008.webp',
        'anim_hardong_2_shower00009.webp',
        'anim_hardong_2_shower00010.webp',
        'anim_hardong_2_shower00011.webp',
        'anim_hardong_2_shower00012.webp',
        'anim_hardong_2_shower00013.webp',
        'anim_hardong_2_shower00014.webp',
        'anim_hardong_2_shower00015.webp',
        'anim_hardong_2_shower00016.webp',
        'anim_hardong_2_shower00017.webp',
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