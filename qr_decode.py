import cv2
from pyzbar.pyzbar import decode


class qr_decoder:
    def decode_once_and_show_frame(self,path):
        # set up camera object
        cap = cv2.VideoCapture(path)

        # Variable that says if has any decodification on the code
        flag = 0

        # Geting the total number of frames in video file
        totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            
        for i in range(int(totalFrames)):
            # get the frame image
            sucess, frame = cap.read()
            
            if sucess == True:
                # Trying to decode any qrcode in frame
                msg = decode(frame)
                    
                if flag >=1:
                    break
                if(msg is not None):
                        
                    for code in msg:

                        # Coordinates of bounding box in qrcode
                        x, y, w, h = code.rect
                        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                        # Decoding de msg of qr code
                        self.barcode_info = code.data.decode('utf-8')

                        # Inserting text in image frame with the decoded msg
                        font = cv2.FONT_HERSHEY_TRIPLEX
                        cv2.rectangle(frame, (x, y),(x+395, y-50), (0, 255, 0), -1)
                        cv2.putText(frame, self.barcode_info, (x + 6, y - 6), font, 2.0, (0, 0, 255), 2)
                            
                        #cv2.namedWindow('Barcode/QR code reader', 0)
                        # Resizing the window shape
                        (width, height) = (int(frame.shape[1]*0.6), int(frame.shape[0]*0.6))
                        dimensions = (width,height)
                        frame_resized = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

                        #Showing the frame with the msg and the bounding box
                        cv2.imshow('Barcode/QR code reader', frame_resized)

                        # Creating .txt file with the msg of qrcode
                        with open("barcode_result.txt", mode ='w') as file:
                            file.write("Recognized Barcode:" + self.barcode_info)
                        flag = flag+ 1
                        if(cv2.waitKey(1000)):
                            break 
           
                if(cv2.waitKey(1) == ord("q")):
                    break
            
        # Verify if there was no one decodification
        if flag == 0:
            print("Could'nt decode any qrcode in this file")

        # free camera object and exit
        cap.release()
        cv2.destroyAllWindows()


    def decode_images(self,path_image):
        # reading img
        img = cv2.imread(path_image)
        msg = decode(img)

        # Show what's in the msg variable
        print(msg)

        # Acessing each element of the list    
        for code in msg:
            print(code.data.decode('utf-8'))
            print(code.type)

    def decode_and_show_all_videoFrames(self,path):
        # set up camera object
        cap = cv2.VideoCapture(path)
  
        # Geting the total number of frames in video file
        totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            
        for i in range(int(totalFrames)):
            # get the frame image
            sucess, frame = cap.read()
            # Resizing frame shape by 0.6
            
                      
            
            if sucess == True:
                
                #Resizing frame by 0.6
                (width, height) = (int(frame.shape[1]*0.6), int(frame.shape[0]*0.6))
                
                dimensions = (width,height)
                frame_resized = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
                # Trying to decode any qrcode in frame
                msg = decode(frame_resized)

                cv2.imshow('Barcode/QR code reader',frame_resized)
                #cv2.waitKey(1)    
                if(msg is not None):
                        
                    for code in msg:

                        # Coordinates of bounding box in qrcode
                        x, y, w, h = code.rect
                        cv2.rectangle(frame_resized, (x, y),(x+w, y+h), (0, 255, 0), 2)
                        # Decoding de msg of qr code
                        self.barcode_info = code.data.decode('utf-8')

                        # Inserting text in image frame with the decoded msg
                        font = cv2.FONT_HERSHEY_TRIPLEX
                        cv2.rectangle(frame_resized, (x, y),(x+395, y-50), (100, 255, 0), -1)

                        (x_text,y_text) = (x+6,y-6)

                        if y_text < 0:
                            y_text = y+h+56
                        
                        cv2.putText(frame_resized, self.barcode_info, (x + 6, y_text), font, 2.0, (0, 0, 255), 2)
                      
                        #Showing the frame with the msg and the bounding box
                        cv2.imshow('Barcode/QR code reader', frame_resized)
                        #cv2.waitKey(1)
                
                    

   
                if(cv2.waitKey(1) == ord("q")):
                    break
      
        # free camera object and exit
        cap.release()
        cv2.destroyAllWindows()