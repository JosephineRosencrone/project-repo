import cv2 
import numpy as np
from matplotlib import pyplot as plt

    
def img_show_each_color_channel(img_path: str):
    # Read the input color image
    img = cv2.imread(img_path)

    # Split the Blue, Green and Red color channels
    blue,green,red = cv2.split(img)

    # Define channel having all zeros
    zeros = np.zeros(blue.shape, np.uint8)

    # Merge zeros to make BGR image
    blueBGR = cv2.merge([blue,zeros,zeros])
    greenBGR = cv2.merge([zeros,green,zeros])
    redBGR = cv2.merge([zeros,zeros,red])

    # Display the three Blue, Green, and Red channels as BGR image
    cv2.imshow('Blue Channel', blueBGR)
    cv2.waitKey(0)
    cv2.imshow('Green Channel', greenBGR)
    cv2.waitKey(0)
    cv2.imshow('Red Channel', redBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Not in use    
def show_before_after_img(img_before, img_after):
    _, axs = plt.subplots(1, 2, figsize=(20, 20))
    plt.subplots_adjust(wspace=0, hspace=0)
    axs[0].imshow(img_before),
    axs[0].set_title('Original')
    axs[0].set_xticks([]), axs[0].set_yticks([])
    axs[1].imshow(img_after)    
    axs[1].set_title('Blurred')
    axs[1].set_xticks([]) 
    axs[1].set_yticks([])

    plt.show()