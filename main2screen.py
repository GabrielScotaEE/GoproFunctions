import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
from secondScreen import *
from time import time
from windowcapture import *
from re import T
from pyzbar.pyzbar import decode
import socket
from decoder import Decode

loop_time = time()
dcd = Decode()
scd = Second_Screen()

while(True):

    screenshot = scd.get_sec_screen()
    opencv_screenshot = np.array(screenshot)

    decode_img, msg = dcd.decode(opencv_screenshot)
    if msg is not None:
        cv.imshow('Qr decodificado', decode_img)
        print('A mensagem do qr code é: {}'.format(msg))
        cv.destroyWindow('Gopro Real Time')
        cv.waitKey(0)
        break


    cv.imshow('Gopro Real Time', opencv_screenshot)
    print('FPS {}'.format(np.round(1/(time()-loop_time))))

    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break