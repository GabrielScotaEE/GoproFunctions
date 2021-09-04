import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
from time import time


class Decode():

    def __init__(self) :

        self.barcode_info = None

        pass

    def decode_pyzbar(self,img):
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
    
      
    def decode_opencv(self,img):
        det = cv.QRCodeDetector()

        retval, points, straight_qrcode = det.detectAndDecode(img)
        
        if not retval:
            retval = None

        else:
            x_min = 100000
            x_max = 0
            y_min = 100000
            y_max = 0
            for i in range (4):
                find_x0, find_x1, find_y0, find_y1 = int(points[0][i][0]), 
                int(points[0][i][0]), 
                int(points[0][i][1]), 
                int(points[0][i][1])

                if find_x0 < x_min:
                    x_min = find_x0
                if find_x1 > x_max:
                    x_max = find_x1
                if find_y0 < y_min:
                    y_min = find_y0
                if find_y1 > y_max:
                    y_max = find_y1
              
            cv.rectangle(img, (x_min, y_min),(x_max, y_max), (0, 255, 0), 2)
            cv.rectangle(img, (x_min, y_min),(x_min+180, y_min-40), (0, 255, 0), -1)
            cv.putText(img, retval, (x_min + 6, y_min - 9), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 1)

        return img, retval, straight_qrcode    

