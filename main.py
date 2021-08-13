import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
from time import time
from windowcapture import *
from re import T
from pyzbar.pyzbar import decode
import socket
from decoder import Decode



# ffplay -fflags nobuffer -f:v mpegts -probesize 8192 udp://@10.5.5.9:8554
# 10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=restart

loop_time = time()

# Creating WindowCapture obj.
# You must give the window name
# without window name, will capture the entire desktop.
wincap = WindowCapture('udp://@10.5.5.9:8554')

# Creating Decode obj.
dcd = Decode()

# Loop through every screenshot creating a video from then

while(True):
    # Call function to keep gopro alive
    wincap.Gopro_Hero_8_keepAlive()
    # Getting the frame of the window with GoPro live.

    #screenshot = wincap.get_sec_screen(1600,900,1368,768)

    screenshot = wincap.get_screenshot()
    opencv_screenshot = np.array(screenshot)
    # Trying to decode any qrcode in th frame
    decode_img, msg, only_qr = dcd.decode_opencv(opencv_screenshot)
    if msg is not None:
        cv.imshow('Gopro Real Time', decode_img)
        
        cv.imshow('Only Qr', only_qr)
        #print('A mensagem do qr code é: {}'.format(msg))
        
    else:
        cv.imshow('Gopro Real Time', opencv_screenshot)
        

    # Showing FPS live.
    print('FPS {}'.format(np.round(1/(time()-loop_time))))

    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

