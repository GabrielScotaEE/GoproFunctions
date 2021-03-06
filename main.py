from decoder import Decode
from gopro_control import GoproClass
from windowcapture import *

# ffplay -fflags nobuffer -f:v mpegts -probesize 8192 udp://@10.5.5.9:8554
# 10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=restart

loop_time = time()

# Creating WindowCapture obj.
# You must give the window name
# without window name, will capture the entire desktop.
wincap = WindowCapture('udp://@10.5.5.9:8554')

# Creating Decode obj.
dcd = Decode()

# creating goproclass obj
goprofunctions = GoproClass()

# Loop through every screenshot creating a video from then

while True:
    # Call function to keep gopro alive
    goprofunctions.gopro_hero8_keep_alive()
    # Getting the frame of the window with GoPro live.

    # screenshot = wincap.get_sec_screen(1600,900,1368,768)

    screenshot = wincap.get_screenshot()
    opencv_screenshot = np.array(screenshot)
    # Trying to decode any qrcode in th frame
    decode_img, msg = dcd.decode_pyzbar(opencv_screenshot)
    if msg is not None:
        cv.imshow('Gopro Real Time', decode_img)

        # cv.imshow('Only Qr', only_qr)
        # print('A mensagem do qr code é: {}'.format(msg))

    else:
        cv.imshow('Gopro Real Time', opencv_screenshot)

    # Showing FPS live.
    print('FPS {}'.format(np.round(1 / (time() - loop_time))))

    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
