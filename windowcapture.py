import cv2 as cv
from pyzbar.pyzbar import decode
import numpy as np
import pyautogui
from time import time
import pywintypes
import win32gui, win32ui, win32con
from PIL import ImageGrab

class WindowCapture:

    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None) :
        
        
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
        # self.w = self.w - (border_pixels*2)
        self.h = self.h - titlebar_pixels - border_pixels
       
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.cropped_x
        self.cropped_y = window_rect[1] + self.cropped_y


        pass
    
    # translate a pixel position on a screenshot image to a pixel position on the screen
    # pos (x,y)
    # WARNING: if you move the window being captured adter execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in __init__
    # def get_screen_position(self,pos):
    #     return (pos[0] + self.offset_x, pos[1] + self.offset_y)

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
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h,self.w,4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        return img

