# GoproFunctions
##  Controling your GoPro Hero 8 by wifi connection

#### This thread will teach you how to connect your gopro in wifi desktop
1. - First, you need to activate wifi in your camera, so click in preferences -> wireless connections -> turn on
2. - Now you can ask yourself why the wifi from your camera isn't in the list of connections on your desktop. This happens because in Hero 8 model the wifi camera is only able to connect to your gopro app. 
   - To connect on your pc, first you need to connect your gopro app to the camera, just folow the steps on app. After establishing connection, you can see that your phone is connected to the wifi camera. **So you only need to come back to the first screen of gopro app**, after that, your wifi camera will appear in your desktop.
3. - Select the wifi from your camera and connect with the password that is show in: preferences -> wireless connections -> info camera

    NOW YOUR ARE ABLE TO CONTROLE YOUR GOPRO BY WIFI 

# Live Stream on Windows Gopro Hero 8 black
## Just Follow the steps below:
1. - You will need ffmpeg player, this link will help with the instalation: (https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows)
2. - Run this code (**WARNING** - The keepAlive function use time.sleep( ) inside a loop, so your code will be lock in this function):
	```
	from goprocam import GoProCamera, constants
	gpc = GoProCamera.GoPro()
	gpc.KeepAlive()
	```
   - *To get a better performance use (this code is in `main.py`)*:
	```
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	last_message = time()
	keep_alive_payload = "_GPHD_:1:0:2:0.000000\n".encode()
	sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))
	```
   - Then keep your gopro alive using:
	```
	while(True):
   	 if current_time - last_message >= 2500/1000:
            sock.sendto(keep_alive_payload, ("10.5.5.9", 8554))
            last_message = current_time
            print('!!!!!!!!!!!!! WAKE UP !!!!!!!!!!!')
	```
3. - Type the folowing url into a browser:  `10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=restart`
4. - Now just use ffplayer (open cmd) to run your live: `ffplay -fflags nobuffer -f:v mpegts -probesize 8192 udp://@10.5.5.9:8554`

