import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
import pyautogui
from time import time
import pywintypes
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab

class Second_Screen():

    def __init__(self):
        self.SM_XVIRTUALSCREEN = 76
        self.SM_YVIRTUALSCREEN = 77
        self.SM_CXVIRTUALSCREEN = 78
        self.SM_CYVIRTUALSCREEN = 79
        self.hwnd = win32gui.GetDesktopWindow()
        pass


    def get_sec_screen(self,full=0):

        w = win32api.GetSystemMetrics(self.SM_CXVIRTUALSCREEN)
        h = win32api.GetSystemMetrics(self.SM_CYVIRTUALSCREEN)
        l = win32api.GetSystemMetrics(self.SM_XVIRTUALSCREEN)
        t = win32api.GetSystemMetrics(self.SM_YVIRTUALSCREEN)

        l=1601
        t=0

        #print (l, t,' -> ', w, h)

        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h),  mfcDC,  (l, t),  win32con.SRCCOPY)

        signedIntsArray = saveBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (h,w,4)

        if full == 1:
            # for full screen
            self.desktop2 = win32gui.GetDesktopWindow()
            x0,y0,x1,y1 = win32gui.GetWindowRect(self.desktop2)
            img = img[y0:y1-132,0:w-x1]
            return img
        else:
            # For GoPro Visualization
            self.preVis_Gopro = win32gui.FindWindow(None, 'Pré-visualização')
            if not self.hwnd:
                raise Exception('Window not found: {}'.format('Pré-visualização'))
            x0,y0,x1,y1 = win32gui.GetWindowRect(self.preVis_Gopro)
            img = img[y0+25:y1-20,25:x1-x0-20]
            return img

        #print(x0,y0,x1,y1)
        # cv.imshow('a',img)
        # cv.waitKey(0)

        

        


sec = Second_Screen()
sec.get_sec_screen(full=1)