import cv2


class Filter:
    def __init__(
        self, kernel_size=(5, 5), blur_method="GaussianBlur", sigma_value=0
    ):
        self.kernel_size = kernel_size
        self.blur_method = blur_method
        self.sigma_value = sigma_value

    def apply_to_image(
        self, img, blur_red=False, blur_green=False, blur_blue=False,
    ):
        # Split the Red, Green, Blue and alpha color channels
        red, green, blue, alpha = cv2.split(img)

        # Blur the color channel if specified
        if blur_red:
            red = self.blur_color_channel(red)
        if blur_green:
            green = self.blur_color_channel(green)
        if blur_red:
            blue = self.blur_color_channel(blue)

        # Create a new image with the blured blue color channel
        img_blur = cv2.merge([red, green, blue])
        return img_blur

    def blur_color_channel(self, color_channel):
        color_channel_blur = color_channel
        if self.blur_method == "GaussianBlur":
            color_channel_blur = cv2.GaussianBlur(
                color_channel, self.kernel_size, self.sigma_value
            )
        elif self.blur_method == "BoxBlur":
            color_channel_blur = cv2.blur(color_channel, self.kernel_size)

        return color_channel_blur
