import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
import pyautogui
import socket
from time import time
import pywintypes
import win32gui, win32ui, win32con, win32api


class WindowCapture():

    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None) :

        self.SM_XVIRTUALSCREEN = 76
        self.SM_YVIRTUALSCREEN = 77
        self.SM_CXVIRTUALSCREEN = 78
        self.SM_CYVIRTUALSCREEN = 79
        
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))


        # get window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # remove window border and title bar
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w  - (border_pixels*2)
        self.h = self.h - titlebar_pixels - border_pixels
       
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

   
        pass
    

    @staticmethod
    def get_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd),win32gui.GetWindowText(hwnd)) 
        win32gui.EnumWindows(winEnumHandler,None)

    def get_screenshot(self):
                             
        # get window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (self.cropped_x,self.cropped_y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h,self.w,4)

        #img = img[35:self.h-8,10:self.w-10]

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        return img

    def get_sec_screen(self,width_first_screen,height_first_screen,widthSecondScreen,heightSecondScreen):

        # width = largura
        w = win32api.GetSystemMetrics(self.SM_CXVIRTUALSCREEN)
        h = win32api.GetSystemMetrics(self.SM_CYVIRTUALSCREEN)
        l = win32api.GetSystemMetrics(self.SM_XVIRTUALSCREEN)
        t = win32api.GetSystemMetrics(self.SM_YVIRTUALSCREEN)
        
        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h),  mfcDC,  (width_first_screen, t),  win32con.SRCCOPY)

        signedIntsArray = saveBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (h,w,4)

        offset_Y = np.absolute(height_first_screen - heightSecondScreen)

       
        # x1 -> width 1st screen // y1 -> height first monitor
        x0,y0,x1,y1 = win32gui.GetWindowRect(self.hwnd)
        
        if (height_first_screen > heightSecondScreen) and (width_first_screen > widthSecondScreen):
            img = img[y0:y1-offset_Y,0:w-x1]
        elif (heightSecondScreen > height_first_screen) and (widthSecondScreen > width_first_screen):
             img = img[y0:y1+offset_Y,0:w-x1]
        

        return img
