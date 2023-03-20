import cv2


def split_and_blur_color_channel(
    img, blur_red=False, blur_green=False, blur_blue=False,
):
    # Split the Red, Green, Blue and alpha color channels
    red, green, blue, alpha = cv2.split(img)

    # Blur the color channel if specified
    if blur_red:
        red = blur_color_channel(red)
    if blur_green:
        green = blur_color_channel(green)
    if blur_red:
        blue = blur_color_channel(blue)

    # Create a new image with the blured blue color channel
    img_blur = cv2.merge([red, green, blue])
    return img_blur


def blur_color_channel(
    color_channel, kernal_size=(5, 5), blur_method="GaussianBlur"
):
    if blur_method == "GaussianBlur":
        color_channel_blur = cv2.GaussianBlur(color_channel, kernal_size, 0)
    else:
        color_channel_blur = cv2.blur(color_channel, kernal_size, 0)

    return color_channel_blur
