import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
import pyautogui
from time import time
from PIL import ImageGrab

class Decode():

    def __init__(self) :

        self.barcode_info = None

        pass

    def decode(self,img):
        msg = decode(img)
        if(msg is not None):
                        
            for code in msg:

                # Coordinates of bounding box in qrcode
                x, y, w, h = code.rect
                cv.rectangle(img, (x, y),(x+w, y+h), (0, 255, 0), 2)
                # Decoding de msg of qr code
                self.barcode_info = code.data.decode('utf-8')

                # Inserting text in image frame with the decoded msg
                font = cv.FONT_HERSHEY_TRIPLEX
                cv.rectangle(img, (x, y),(x+395, y-50), (0, 255, 0), -1)
                cv.putText(img, self.barcode_info, (x + 6, y - 6), font, 2.0, (0, 0, 255), 2)
                
        return img, self.barcode_info
        