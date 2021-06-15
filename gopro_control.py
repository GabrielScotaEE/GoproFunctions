from goprocam import GoProCamera, constants
import cv2
import urllib.request
from PIL import Image
import shutil
import os
from skimage.io import imread_collection
import numpy as np


# Creating obj gopro
goproCamera = GoProCamera.GoPro()

class GP_functions:

    def __init__(self,folder='./images/*.JPG'):
        self.folder_location = folder
        pass

    def url_image_show(self):
        # get photo location
        location = goproCamera.getMedia()
        urllib.request.urlretrieve(location, "GOPR0293.JPG")
        img = Image.open("GOPR0293.JPG")
        img.show()

    def take_photo_download_and_delete(self):
        goproCamera.take_photo(timer=3)
        goproCamera.downloadLastMedia
        goproCamera.delete("last")

    def media_download_and_change_directory(self):
        # downloadAll returns a list of all images, videos... in the camera
        media = goproCamera.downloadAll()
        # moving images to a specific folder /images
        for i in media:
            shutil.move('./100GOPRO-{}'.format(i), './images/{}'.format(i))

    def load_img_from_folder(self,folder):
        self.images_list = imread_collection(folder)
       
        
    def load_videos_from_folder(self,folder):
        self.videos_list = imread_collection(folder)

    def show_some_downloadeds_imgs(self):
        cv2.namedWindow('sample image', 0)
        for i in range(len(gopro_functions.images_list)):
            img = (gopro_functions.images_list[i])
            cv2.imshow('sample image',img)
            cv2.waitKey(0)
    
    def show_some_downloadeds_videos(self):
        # Create a VideoCapture object and read from input file
        video_name_file = os.listdir('.\images')[0]
        
        cap = cv2.VideoCapture('.\images\{}'.format(video_name_file))

        # Check if camera opened successfully
        if (cap.isOpened()== False):
            print("Error opening video file")

            # Read until video is completed
        while(cap.isOpened()):
                
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:

            # Display the resulting frame
                cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break



        # When everything done, release
        # the video capture object
        cap.release()

        # Closes all the frames
        cv2.destroyAllWindows()
                    
       
         


gopro_functions = GP_functions()

#goproCamera.video_settings(res="1080",fps="30")
#goproCamera.shoot_video(duration=5)
#gopro_functions.media_download_and_change_directory()
#goproCamera.delete("all")
#gopro_functions.load_img_from_folder('.\images\*.JPG')
#print(gopro_functions.images_list)
#gopro_functions.load_videos_from_folder('.\images\*.MP4')
#print(gopro_functions.videos_list)


#gopro_functions.show_some_downloadeds_imgs()
gopro_functions.show_some_downloadeds_videos()




