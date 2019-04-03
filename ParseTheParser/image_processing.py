import pyautogui
from data import NUMBERS_0_10


def get_screenshot_with_size(up_from_left=0, up_from_top=0, d_from_left=1920, d_from_top=1080):
    """ Default values for 1920x1080. Returns image and its size """
    screenshot = pyautogui.screenshot(region=(up_from_left, up_from_top, d_from_left, d_from_top))
    width = d_from_left - up_from_left
    height = d_from_top - up_from_top
    return screenshot, (width, height)


def get_image_data(image_data=()):
    """
    :param image_data: tuple (screenshot, (width, height))
    :return: dict {(pixel_coordinates): (rgb_info), ...}; ex. {(0, 0): (240, 240, 240), (0, 1): (240, 240, 240), ...}
    """
    width, height = image_data[1]
    img_data = {}
    for wdth_pix in range(width+1):
        for lngth_pix in range(height+1):
            val = image_data[0].getpixel((wdth_pix, lngth_pix))
            img_data[(wdth_pix, lngth_pix)] = val
    return img_data

# # Test of functions get_screenshot_with_size + get_image_data: for recognition of 0 (passed, others too)
# screenshot = get_screenshot_with_size(465, 51, 474, 73)
# print(screenshot)
# print(get_image_data(screenshot))
# print(get_image_data(screenshot) == NUMBERS_0_10[0])

# screenshot = get_screenshot_with_size(553, 311, 628, 318)
# print(screenshot)
# print(get_image_data(screenshot))


def recognize_number(scrnshot):
    """ Recognizes and returns number at coordinates (465, 51, 474, 73) based on collected data """
    recognized_num = False
    for number in range(0, 11):
        if get_image_data(scrnshot) == NUMBERS_0_10[number]:
            recognized_num = number
    return recognized_num

# screen_now = get_screenshot_with_size(465, 51, 474, 73)
# print(recognize_number(screen_now))


def await_image(image_file):
    isfound = pyautogui.locateOnScreen(image_file, minSearchTime=60)
    if isfound:
        return True
    else:
        return False

# print(await_image('znaleziono2.png'))




