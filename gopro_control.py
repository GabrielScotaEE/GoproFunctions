from goprocam import GoProCamera, constants
import cv2
import urllib.request
from PIL import Image
import shutil
import os
from skimage.io import imread_collection
import numpy as np
from pyzbar.pyzbar import decode
from qr_decode import QRdecoder
import time
import socket


class GoproClass():
    

    def __init__(self,folder='./images'):
        self.folder_location = folder
        #self.goproCamera = GoProCamera.GoPro()
        pass

    def url_image_show(self):
        # get photo location
        location = self.goproCamera.getMedia()
        urllib.request.urlretrieve(location, "GOPR0293.JPG")
        img = Image.open("GOPR0293.JPG")
        img.show()

    def take_photo_download_and_delete(self):
        goproCamera.take_photo(timer=3)
        goproCamera.downloadLastMedia
        goproCamera.delete("last")

    def downloadAndChangeDirectory(self):
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
    
    def show_downloadedVideoFiles(self):
        
        self.videos_list = []
        # Creating a list with all files in 
        list_files = os.listdir(self.folder_location)
        # Filtering only .mp4 files
        for video in list_files:
            print(video)
            if video.find('.MP4')>0:
                self.videos_list.append(video)       
        return self.videos_list

    def GoproHero8_keepAlive(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        last_message = time.time()
        keep_alive_payload = "_GPHD_:1:0:2:0.000000\n".encode()
        sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))

        # keep gopro alive
        current_time = time.time()
        if current_time - last_message >= 2500/1000:
            sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))
            last_message = current_time
            print('!!!!!!!!!!!!! WAKE UP !!!!!!!!!!!!!')




#begin = time.time()
#end = time.time()
#print('A funçao demora: {} segundos'.format(end-begin))


# goproFunct = GoproClass()
#goproCamera.shoot_video(duration=5)
#goproFunct.media_download_and_change_directory()
#goproCamera.delete("all")
#goproCamera.take_photo(timer=2)
#goproFunct.show_downloaded_imgs()

#goproFunct.media_download_and_change_directory()
#goproCamera.getStatus("Battery",value="1")

#decoder = qr_decoder
#decoder.decode_and_show_all_videoFrames(decoder,'./images/GH010302.MP4')
#decoder.decode_once_and_show_frame(decoder,'./images/GH010302.MP4')





