from goprocam import GoProCamera, constants
import cv2
import urllib.request
from PIL import Image
import shutil
import os
from skimage.io import imread_collection
import numpy as np
from pyzbar.pyzbar import decode


# Creating obj gopro
#goproCamera = GoProCamera.GoPro()

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

    def try_to_decode_and_show_frame_if_is_decoded(self,path):
            # set up camera object
            cap = cv2.VideoCapture(path)

            # Variable that says if has any decodification on the code
            flag = 0

            # Geting the total number of frames in video file
            totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            
            for i in range(int(totalFrames)):
                # get the frame image
                sucess, frame = cap.read()
            
                if sucess == True:
                    # Trying to decode any qrcode in frame
                    msg = decode(frame)
                    
                    if flag >=1:
                        break
                    if(msg is not None):
                        
                        for code in msg:

                            # Coordinates of bounding box in qrcode
                            x, y, w, h = code.rect
                            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                            # Decoding de msg of qr code
                            self.barcode_info = code.data.decode('utf-8')

                            # Inserting text in image frame with the decoded msg
                            font = cv2.FONT_HERSHEY_TRIPLEX
                            cv2.rectangle(frame, (x, y),(x+395, y-50), (0, 255, 0), -1)
                            cv2.putText(frame, self.barcode_info, (x + 6, y - 6), font, 2.0, (0, 0, 255), 2)
                            
                            #cv2.namedWindow('Barcode/QR code reader', 0)
                            # Resizing the window shape
                            width = int(frame.shape[1]*0.6)
                            height = int(frame.shape[0]*0.6)
                            dimensions = (width,height)
                            frame_resized = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

                            #Showing the frame with the msg and the bounding box
                            cv2.imshow('Barcode/QR code reader', frame_resized)

                            # Creating .txt file with the msg of qrcode
                            with open("barcode_result.txt", mode ='w') as file:
                                file.write("Recognized Barcode:" + self.barcode_info)
                            flag = flag+ 1
                            if(cv2.waitKey(0)):
                                break 
           
                    if(cv2.waitKey(1) == ord("q")):
                        break
            # Verify if there was no one decodification
            if flag == 0:
                print("Could'nt decode any qrcode in this file")

            # free camera object and exit
            cap.release()
            cv2.destroyAllWindows()
                    
       
         


gopro_functions = GP_functions()

gopro_functions.try_to_decode_and_show_frame_if_is_decoded('GH010308.MP4')


#goproCamera.video_settings(res="1080",fps="30")
#goproCamera.shoot_video(duration=5)
#gopro_functions.media_download_and_change_directory()
#goproCamera.delete("all")
#gopro_functions.load_img_from_folder('.\images\*.JPG')
#print(gopro_functions.images_list)
#gopro_functions.load_videos_from_folder('.\images\*.MP4')
#print(gopro_functions.videos_list)
#goproCamera.take_photo(timer=2)
#gopro_functions.show_some_downloadeds_imgs()
#gopro_functions.show_some_downloadeds_videos()




