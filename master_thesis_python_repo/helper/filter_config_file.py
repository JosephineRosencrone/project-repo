import cv2
import numpy as np
import win32gui
from master_thesis_python_repo.helper.import_config import FilterSettings


class Filter_With_Config:
    def __init__(self, filter_settings: FilterSettings):
        self.filter_settings = filter_settings

    def apply_to_image(self, img, nonBlurRadius=0):
        # Split the Red, Green, Blue and alpha color channels
        red, green, blue, alpha = cv2.split(img)
        
        # Blur the color channel 
        red = self.blur_color_channel(red, 2, nonBlurRadius)
        green = self.blur_color_channel(green, 1, nonBlurRadius)
        blue = self.blur_color_channel(blue, 0, nonBlurRadius)

        # Create a new image with the blured blue color channel
        img_blur = cv2.merge([red, green, blue])
        
        return img_blur


    def blur_color_channel(self, color_channel_data, color_channel_id, radius):
        color_channel_blur = color_channel_data
        
        if self.filter_settings.settings[color_channel_id].sigma == 0:
            return color_channel_data

        kernel_value = self.filter_settings.settings[color_channel_id].kernelSize
        for _ in range(0, self.filter_settings.settings[color_channel_id].timeFiltersApllied):
            if self.filter_settings.settings[color_channel_id].filterType == "gauss":
                # create circular mask
                _, _, (cursorX, cursorY) = win32gui.GetCursorInfo()
                height, width = color_channel_data.shape[:2]
                mask = np.zeros((height, width), dtype=np.uint8)
                cv2.circle(mask, (cursorX, cursorY), radius, 255, -1)
                
                # apply blur only outside the circular mask
                blur = cv2.GaussianBlur(
                    cv2.bitwise_and(color_channel_blur, color_channel_blur, mask=cv2.bitwise_not(mask)),
                    (kernel_value, kernel_value), self.filter_settings.settings[color_channel_id].sigma, None, self.filter_settings.settings[color_channel_id].sigma2
                )
                color_channel_blur = cv2.bitwise_or(blur, cv2.bitwise_and(color_channel_blur, color_channel_blur, mask=mask))
                
            elif self.filter_settings.settings[color_channel_id].filterType == "boxBlur":
                blur = cv2.blur(color_channel_blur, self.filter_settings.settings[color_channel_id].kernelSize)
                color_channel_blur = blur

        if self.filter_settings.settings[color_channel_id].blurOrSharpenCheckbox:
            color_channel_blur = cv2.addWeighted(color_channel_data, 1.5, color_channel_blur, -0.5, 0)
            color_channel_blur = cv2.normalize(color_channel_blur, None, 0, 255, cv2.NORM_MINMAX)

        return color_channel_blur


    def blur_color_channel_old(self, color_channel_data, color_channel_id):
        color_channel_blur = color_channel_data
        
        if self.filter_settings.settings[color_channel_id].sigma == 0:
            return color_channel_data
        
        
        kernel_value = self.filter_settings.settings[color_channel_id].kernelSize
        for _ in range(0, self.filter_settings.settings[color_channel_id].timeFiltersApllied):
            if self.filter_settings.settings[color_channel_id].filterType == "gauss":
                blur = cv2.GaussianBlur(
                    color_channel_blur, (kernel_value, kernel_value), self.filter_settings.settings[color_channel_id].sigma, None, self.filter_settings.settings[color_channel_id].sigma2
                )
            elif self.filter_settings.settings[color_channel_id].filterType == "boxBlur":
                blur = cv2.blur(color_channel_blur, self.filter_settings.settings[color_channel_id].kernelSize)

        if self.filter_settings.settings[color_channel_id].blurOrSharpenCheckbox:
            color_channel_blur = cv2.addWeighted(color_channel_blur, 1.5, blur, -0.5, 0)
            color_channel_blur = cv2.normalize(color_channel_blur, None, 0, 255, cv2.NORM_MINMAX)
        else:
            color_channel_blur = blur
        
        return color_channel_blur
