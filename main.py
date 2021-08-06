import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np

from time import time
from windowcapture import *
from re import T
from pyzbar.pyzbar import decode
import socket
from decoder import Decode

loop_time = time()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

last_message = time()
keep_alive_payload = "_GPHD_:1:0:2:0.000000\n".encode()
sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))

# ffplay -fflags nobuffer -f:v mpegts -probesize 8192 udp://@10.5.5.9:8554
# 10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=restart

while(True):
    hwnd = win32gui.FindWindow(None, 'udp://@10.5.5.9:8554')
    if not hwnd:
        print('Window not found: {}'.format('udp://@10.5.5.9:8554'))
        current_time = time()
        if current_time - last_message >= 2500/1000:
            sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))
            last_message = current_time
            print('!!!!!!!!!!!!! WAKE UP !!!!!!!!!!!')
        
    else: break
    # keep gopro alive
    

wincap = WindowCapture('udp://@10.5.5.9:8554')
dcd = Decode()

while(True):
    
    # keep gopro alive
    current_time = time()
    if current_time - last_message >= 2500/1000:
                sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))
                last_message = current_time
                print('!!!!!!!!!!!!! WAKE UP !!!!!!!!!')

    screenshot = wincap.get_screenshot()
    opencv_screenshot = np.array(screenshot)

    decode_img, msg = dcd.decode(opencv_screenshot)
    if msg is not None:
        cv.imshow('Gopro Real Time', decode_img)
        #print('A mensagem do qr code é: {}'.format(msg))
        break
        
    else:
        cv.imshow('Gopro Real Time', opencv_screenshot)
        


    print('FPS {}'.format(np.round(1/(time()-loop_time))))

    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

pass