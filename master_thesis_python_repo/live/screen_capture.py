import time

import cv2
import mss
import numpy as np
from matplotlib import pyplot as plt

from master_thesis_python_repo.helper.filter import Filter


class Screen_Capture:
    def __init__(self, name, screen_width, screen_height):
        self.name = name
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.filter = Filter()

    def nothing(self, x):
        pass

    def run(self):
        with mss.mss() as sct:
            # Define the part of the screen to capture
            monitor = {
                "top": 0,
                "left": 0,
                "width": self.screen_width,
                "height": self.screen_height,
            }
            windowName = "OpenCV/Numpy blur"

            # Create a black image, a window
            img = np.zeros((800, 800, 3), np.uint8)
            cv2.namedWindow(windowName)

            # Create UI elements
            switch = "0 : OFF \n 1 : ON"
            kernelSizeName = "Kernel Size"
            blurType = "Blur Type"
            sigmaValueName = "Sigma value"
            cv2.createTrackbar(kernelSizeName, windowName, 0, 20, self.nothing)
            cv2.createTrackbar(sigmaValueName, windowName, 0, 20, self.nothing)
            cv2.createTrackbar(blurType, windowName, 1, 2, self.nothing)
            cv2.createTrackbar(switch, windowName, 0, 1, self.nothing)

            # Turn on interactive mode for Matplotlib
            plt.ion()

            # Create the plot
            fig, ax = plt.subplots()
            (lineR,) = ax.plot(range(self.screen_width))
            (lineG,) = ax.plot(range(self.screen_width))
            (lineB,) = ax.plot(range(self.screen_width))
            ax.set_ylim(0, 255)

            while "Screen capturing":
                # Capture time for debugging
                last_time = time.time()

                # Get raw pixels from the screen, save it to a Numpy array
                img = np.array(sct.grab(monitor))

                # Get switch state
                s = cv2.getTrackbarPos(switch, windowName)

                # If switch is on use filter, else show un-processed image
                blur_method = ""
                if s == 1:
                    # Get kernel size value
                    kernel_size = cv2.getTrackbarPos(
                        kernelSizeName, windowName
                    )
                    if kernel_size % 2 == 0:
                        kernel_size += 1

                    # Get sigma value
                    sigma_value = cv2.getTrackbarPos(
                        sigmaValueName, windowName
                    )
                    sigma_value /= 10

                    # Get blur filter method
                    blur_index = cv2.getTrackbarPos(blurType, windowName)
                    if blur_index == 0:
                        blur_method = "GaussianBlur"
                    elif blur_index == 1:
                        blur_method = "BoxBlur"
                    else:
                        break

                    # Blur image
                    self.filter.kernel_size = (kernel_size, kernel_size)
                    self.filter.blur_method = blur_method
                    self.filter.sigma_value = sigma_value
                    img_final = self.filter.apply_to_image(
                        img=img, blur_blue=True, blur_green=True, blur_red=True
                    )
                else:
                    img_final = img

                # Display the picture
                cv2.putText(
                    img_final,
                    blur_method,
                    (00, 185),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )
                cv2.imshow(windowName, img_final)

                print(f"fps: {1 / (time.time() - last_time)}")

                # Press "q" to quit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

                # Get the 10th row of the image

                row = img_final[round(len(img_final) / 2), :]
                r_array = [inner[0] for inner in row]
                g_array = [inner[1] for inner in row]
                b_array = [inner[2] for inner in row]
                # Update the plot
                lineR.set_ydata(r_array)
                lineG.set_ydata(g_array)
                lineB.set_ydata(b_array)
                plt.draw()
                plt.pause(0.01)
