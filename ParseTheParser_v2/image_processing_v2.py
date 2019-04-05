import pyautogui
import datetime
from data_v2 import NUMBERS_0_10


# for future: https://github.com/Hermotimos/practical_programs/compare/messy?expand=1
nowe_0 = '.\\nowe_0.png'
nowe_1 = '.\\nowe_1.png'
nowe_2 = '.\\nowe_2.png'
nowe_3 = '.\\nowe_3.png'
nowe_4 = '.\\nowe_4.png'
nowe_5 = '.\\nowe_5.png'
nowe_6 = '.\\nowe_6.png'
nowe_7 = '.\\nowe_7.png'
nowe_8 = '.\\nowe_8.png'
nowe_9 = '.\\nowe_9.png'
nowe_10 = '.\\nowe_10.png'
numbers_imgs = (nowe_0, nowe_1, nowe_2, nowe_3, nowe_4, nowe_5, nowe_6, nowe_7, nowe_8, nowe_9, nowe_10)


def try_recognize_number(screenshot):
    num = recognize_number(screenshot)
    if num:
        return num
    else:
        now = datetime.datetime.now()
        print("{}: Number at position 'Nowe' not recognized. "
              "\nTry to determine the cause for future development.".format(now))
        return num


def recognize_number():
    recognized_num = False
    for num, num_img in enumerate(numbers_imgs):
        if pyautogui.locateOnScreen:
            recognized_num = num
    return recognized_num



# def get_screenshot_with_size(up_from_left=0, up_from_top=0, d_from_left=1920, d_from_top=1080):
#     screenshot = pyautogui.screenshot(region=(up_from_left, up_from_top, d_from_left, d_from_top))
#     width = d_from_left - up_from_left
#     height = d_from_top - up_from_top
#     return screenshot, (width, height)
#
#
# def get_image_data(image_with_size=()):
#     """ returns dict ((pixel_coordinates): (rgb_info), ...)
#     ex. {(0, 0): (240, 240, 240), (0, 1): (240, 240, 240), ...} """
#     width, height = image_with_size[1]
#     img_data = {}
#     for wdth_pix in range(width+1):
#         for lngth_pix in range(height+1):
#             val = image_with_size[0].getpixel((wdth_pix, lngth_pix))
#             img_data[(wdth_pix, lngth_pix)] = val
#     return img_data


def await_image(image_file, seconds=30):
    isfound = pyautogui.locateOnScreen(image_file, minSearchTime=seconds)
    if isfound:
        return True
    else:
        return False


def try_go_to_image(image):
    try:
        go_to_image(image)
    except TypeError:
        try_go_to_image(image)


def go_to_image(image):
    location = pyautogui.locateOnScreen(image)
    center = pyautogui.center(location)
    pyautogui.moveTo(center[0], center[1], duration=0.5)


# TESTS
#
# screen_now = get_screenshot_with_size(465, 51, 474, 73)
# print(recognize_number(screen_now))
#
# # Test of functions get_screenshot_with_size + get_image_data: for recognition of 0 (passed)
# screenshot = get_screenshot_with_size(465, 51, 474, 73)
# print(screenshot)
# print(get_image_data(screenshot))
# print(get_image_data(screenshot) == NUMBERS_0_10[0])

# screenshot = get_screenshot_with_size(553, 311, 628, 318)
# print(screenshot)
# print(get_image_data(screenshot))

print(pyautogui.locateOnScreen('.\\status_button.png'))
print(pyautogui.locateOnScreen('.\\nowe_0.png'))
print(pyautogui.locateOnScreen('.\\nowe_1.png'))
