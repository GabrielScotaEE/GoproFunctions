from goprocam import GoProCamera, constants
import cv2
import urllib.request
from PIL import Image
import shutil
import os
from skimage.io import imread_collection


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
       
         





gopro_functions = GP_functions()

#goproCamera.shoot_video(duration=5)
#gopro_functions.media_download_and_change_directory()
gopro_functions.load_img_from_folder('.\images\*.JPG')
print(gopro_functions.images_list)
gopro_functions.load_videos_from_folder('.\images\*.MP4')
print(gopro_functions.videos_list)





