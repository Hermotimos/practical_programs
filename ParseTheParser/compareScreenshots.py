import pyautogui
import time
from data import NUMBERS_LIST


# def get_image_dimensions(image):                    # there's a problem with encoding
#     from PIL import Image
#     width, heigth = Image.open(open(image)).size
#     return width, heigth
# print(get_image_dimensions('example.png'))


def get_image_data(image):

    img_data = {}
    for wdth_pix in range(10):
        for lngth_pix in range(23):
            val = image.getpixel((wdth_pix, lngth_pix))
            img_data[(wdth_pix, lngth_pix)] = val
    return img_data


screenshot = pyautogui.screenshot(region=(465, 51, 474, 73))
print(get_image_data(screenshot))


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


screen_now = pyautogui.screenshot(region=(465, 51, 474, 73))
print(recognize_number(screen_now))









