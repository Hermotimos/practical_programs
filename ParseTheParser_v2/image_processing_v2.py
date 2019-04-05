import pyautogui
import datetime

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
nowe_numbers = (nowe_0, nowe_1, nowe_2, nowe_3, nowe_4, nowe_5, nowe_6, nowe_7, nowe_8, nowe_9, nowe_10)


def try_recognize_number():
    num = recognize_number()
    try:
        assert -1 < num < 11
        return num
    except Exception as e:
        now = datetime.datetime.now()
        print("{}: Number at position 'Nowe' not recognized: {}".format(now.strftime('%H:%M:%S'), e))
        return 0


def recognize_number():
    recognized_num = -1
    for number, image in enumerate(nowe_numbers):
        if pyautogui.locateOnScreen(image):
            recognized_num = number
    return recognized_num


def await_image(image_file, seconds=30):
    isfound = pyautogui.locateOnScreen(image_file, minSearchTime=seconds)
    if isfound:
        return True
    else:
        return False


def try_go_to_image(image, err_cnt=0):
    name = image[2:].split('.')[0]
    try:
        if err_cnt == 0:
            print('try: {:15} {:3}'.format(name, err_cnt), end='')
        go_to_image(image)
    except TypeError:
        err_cnt += 1
        print('{}try: {:15} {:3}'.format('\b'*25, name, err_cnt), end='')
        try_go_to_image(image, err_cnt)


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
