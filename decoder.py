from math import ceil

import cv2 as cv
from pyzbar.pyzbar import decode


class Decode:

    def __init__(self):

        self.barcode_info = None

        pass

    def decode_pyzbar(self, img):
        msg = decode(img)
        if msg is not None:

            for code in msg:
                # Coordinates of bounding box in qrcode
                x, y, w, h = code.rect
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Decoding de msg of qr code
                self.barcode_info = code.data.decode('utf-8')

                # Inserting text in image frame with the decoded msg
                font = cv.FONT_HERSHEY_TRIPLEX
                cv.rectangle(img, (x, y), (x + 395, y - 50), (0, 255, 0), -1)
                cv.putText(img, self.barcode_info, (x + 6, y - 6), font, 2.0, (0, 0, 255), 2)

        return img, self.barcode_info

    @staticmethod
    def decode_opencv(img):
        det = cv.QRCodeDetector()

        msg, points, straight_qrcode = det.detectAndDecode(img)

        if not msg:
            msg = None

        else:
            points = points[0]
            for idx in range(len(points)):
                pt1 = [int(val) for val in points[idx]]
                pt2 = [int(val) for val in points[(idx + 1) % 4]]
                cv.line(img, pt1, pt2, color=(0, 255, 0), thickness=3)
                if idx == 1:
                    xmin = ceil(pt1[0]/7)
                if idx == 2:
                    ymin = ceil(pt1[1]/1.8)
            cv.putText(img, msg, (xmin, ymin), cv.FONT_HERSHEY_TRIPLEX, 0.6, (0, 150, 255), thickness=2)

        return img, msg, straight_qrcode
