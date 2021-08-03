from goprocam import GoProCamera, constants
import cv2
import urllib.request
from PIL import Image
import shutil
import os
from skimage.io import imread_collection
import numpy as np
from pyzbar.pyzbar import decode
from qr_decode import qr_decoder
import time


# Creating obj gopro
#goproCamera = GoProCamera.GoPro()

class GP_functions:
    

    def __init__(self,folder='./images'):
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
        goproCamera.delete("all")

    def show_downloaded_imgs(self):
        cv2.namedWindow('sample image', 0)
        image_list =[]
        list_files = os.listdir(self.folder_location)
        for files in list_files:
            if files.find('.MP4')<0:
                image_list.append(files) 
        for images in image_list:
            img = cv2.imread('.\images\{}'.format(images))
            cv2.imshow('sample image',img)
            cv2.waitKey(0)
    
    def show_downloaded_videos(self):
        
        self.videos_list = []
        # Creating a list with all files in 
        list_files = os.listdir(self.folder_location)
        # Filtering only .mp4 files
        for video in list_files:
            if video.find('.MP4')>0:
                self.videos_list.append(video)       

        for video_name in self.videos_list:
            # Create a VideoCapture object and read from input file
            cap = cv2.VideoCapture('.\images\{}'.format(video_name))

                # Check if camera opened successfully
            if (cap.isOpened()== False):
                print("Error opening video file")

                # Read until video is completed
            while(cap.isOpened()):
                        
                # Capture frame-by-frame
                ret, frame = cap.read()
                
                if ret == True:
                    (width, height) = (int(frame.shape[1]*0.6), int(frame.shape[0]*0.6))
                    dimensions = (width,height)
                    frame_resized = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
                # Display the resulting frame
                    cv2.imshow('Frame', frame_resized)

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




#begin = time.time()
#end = time.time()
#print('A funçao demora: {} segundos'.format(end-begin))


#gopro_functions = GP_functions()
#goproCamera.shoot_video(duration=5)
#gopro_functions.media_download_and_change_directory()
#goproCamera.delete("all")
#goproCamera.take_photo(timer=2)
#gopro_functions.show_downloaded_imgs()
#gopro_functions.show_downloaded_videos() 
#gopro_functions.media_download_and_change_directory()
#goproCamera.getStatus("Battery",value="1")

decoder = qr_decoder
#decoder.decode_and_show_all_videoFrames(decoder,'./images/GH010302.MP4')
decoder.decode_once_and_show_frame(decoder,'./images/GH010302.MP4')





