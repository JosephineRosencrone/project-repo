import time

import cv2
import mss
import numpy as np

from master_thesis_python_repo.helper.image_blur import (
    split_and_blur_color_channel,
)


def nothing(x):
    pass


def screen_capture_test():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 0, "left": 0, "width": 800, "height": 800}
        windowName = "OpenCV/Numpy blur"

        # Create a black image, a window
        img = np.zeros((800, 800, 3), np.uint8)
        cv2.namedWindow(windowName)

        # Create UI elements
        switch = "0 : OFF \n1 : ON"
        kernalSize = "kernalSize"
        blurType = "blurType"
        cv2.createTrackbar(kernalSize, windowName, 0, 255, nothing)
        cv2.createTrackbar(blurType, windowName, 1, 2, nothing)
        cv2.createTrackbar(switch, windowName, 0, 1, nothing)

        while "Screen capturing":
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))

            # Get switch state
            s = cv2.getTrackbarPos(switch, windowName)

            # If switch is on use filter, else show un-processed image
            if s == 0:
                # Get kernal size value
                kernal_size = cv2.getTrackbarPos(kernalSize, windowName)
                if kernal_size % 2 == 0:
                    kernal_size += 1
                # TODO: kernal = (kernal_size, kernal_size)

                # Get blur filter method
                # blur_index = cv2.getTrackbarPos(blurType, windowName)
                # match blur_index:
                #     case 0:
                #         blur_method = "GaussianBlur"
                #     case 1:
                #         blur_method = "Blur"
                blur_method = "GaussianBlur"
                # Blur image

                img_blur = split_and_blur_color_channel(
                    img=img, blur_blue=True
                )
            else:
                img_blur = img

            # Display the picture
            cv2.putText(
                img_blur,
                blur_method,
                (00, 185),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            cv2.imshow(windowName, img_blur)

            print(f"fps: {1 / (time.time() - last_time)}")

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
