import numpy as np
import win32gui, win32ui
from PIL import Image

def set_pixel(img, x, y, rgb=(0,0,0)):
    # Get the shape of the image
    img_h, img_w, _ = np.shape(img)

    # Check if pixel is outside the capture window
    if x>=img_w or y >= img_h:
        return img 
    
    # Upldate the pixel rgb value
    img[x][y][0:3] = rgb
    return img

def add_mouse(img):
    # Fetch cursor information
    _, hcursor, (cx,cy) = win32gui.GetCursorInfo()
    cursor = get_cursor(hcursor)
    cursor_mean = cursor.mean(-1)
    where = np.where(cursor_mean>0)
    
    # Loop over the cursor pixels and create the mouse
    for x, y in zip(where[0], where[1]):
        rgb = [x for x in cursor[x,y]]
        img = set_pixel(img, x+cy, y+cx, rgb=rgb)
    return img


def get_cursor(hcursor):    
    # Fetch cursor information
    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, 36, 36)
    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0,0), hcursor)
    
    bmpinfo = hbmp.GetInfo()
    bmpbytes = hbmp.GetBitmapBits()
    bmpstr = hbmp.GetBitmapBits(True)
    im = np.array(Image.frombuffer(
        'RGB',
         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
         bmpstr, 'raw', 'BGRX', 0, 1))
    
    win32gui.DestroyIcon(hcursor)    
    win32gui.DeleteObject(hbmp.GetHandle())
    hdc.DeleteDC()
    return im