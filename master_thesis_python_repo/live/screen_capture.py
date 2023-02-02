
import time
import cv2
import numpy as np
import mss

from helper.image_blur import blur_blue_channel

def nothing(x):
    pass


def screen_capture_test():
    with mss.mss() as sct:
        global text_test
        # Part of the screen to capture
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        windowName = "OpenCV/Numpy blur"
        
        7 # Create a black image, a window
        img = np.zeros((1920,1080,3), np.uint8)
        cv2.namedWindow(windowName)
        cv2.createTrackbar("KernalSize",windowName,0,255, nothing)
        cv2.createTrackbar("blurType",windowName,1,2, nothing)
         # create switch for ON/OFF functionality
        switch = '0 : OFF \n1 : ON'
        cv2.createTrackbar(switch, windowName,0,1, nothing)
    
        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            
            img = np.array(sct.grab(monitor))
            
            s = cv2.getTrackbarPos(switch,windowName)
            if s == 0:
                kernal_size = cv2.getTrackbarPos("KernalSize", windowName)
                if kernal_size % 2 == 0:
                    kernal_size += 1
                kernal = (kernal_size, kernal_size)
                
                blur_index = cv2.getTrackbarPos("blurType", windowName)
                match blur_index:
                    case 0:    
                        blur_method = "GaussianBlur"
                    case 1:
                        blur_method = "Blur"
                
                img_blur = blur_blue_channel(img, kernal, blur_method=blur_method)
            else:
                img_blur = img
            # Display the picture
            # cv2.imshow("OpenCV/Numpy normal", img)
            
            cv2.putText(img_blur, blur_method, (00, 185), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.imshow(windowName, img_blur)
            
            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

            print(f"fps: {1 / (time.time() - last_time)}")

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
            
screen_capture_test()

    
    
def pil_frombytes(im):
    """ Efficient Pillow version. """
    print("hej")
    #return Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX').tobytes()