import pyautogui
import time
from data import NUMBERS_LIST


# def get_image_dimensions(image):                    # there's a problem with encoding
#     from PIL import Image
#     width, heigth = Image.open(open(image)).size
#     return width, heigth
# print(get_image_dimensions('example.png'))


def screenshot_1920x1080(up_from_left=0, up_from_top=0, d_from_left=1920, d_from_top=1080):
    screenshot = pyautogui.screenshot(region=(up_from_left, up_from_top, d_from_left, d_from_top))
    width = d_from_left - up_from_left
    height = d_from_top - up_from_top
    return screenshot, (width, height)


def get_image_data(image_with_size=()):
    width, height = image_with_size[1]
    img_data = {}
    for wdth_pix in range(width+1):
        for lngth_pix in range(height+1):
            val = image_with_size[0].getpixel((wdth_pix, lngth_pix))
            img_data[(wdth_pix, lngth_pix)] = val
    return img_data

# # Test of functions screenshot_1920x1080 + get_image_data: for 0 recognition (passed)
# screenshot = screenshot_1920x1080(465, 51, 474, 73)
# print(screenshot)
# print(get_image_data(screenshot))
# print(get_image_data(screenshot) == NUMBERS_LIST[0])


def compare_images(img_data1, img_data2):
    time.sleep(3)                           # todo remove this line when ready, now to switch windows
    if img_data1 == img_data2:
        return True
    else:
        return False


def recognize_number(scrnshot):
    result = False
    for number in range(0, 11):
        if get_image_data(scrnshot) == NUMBERS_LIST[number]:
            result = number
    return result


# screen_now = pyautogui.screenshot(region=(465, 51, 474, 73))
# print(recognize_number(screen_now))









