import pyautogui
import time
from image_processing import recognize_number, await_image, get_screenshot_with_size


pyautogui.PAUSE = 0.1                   # sets pause between function calls to n secs
pyautogui.FAILSAFE = True               # possible escape by moving cursor to upper left corner of screen


def correct_scrollbar():
    pyautogui.moveTo(1906, 193, duration=0.5)
    pyautogui.click()


def click_search():
    pyautogui.moveTo(1185, 813, duration=0.5)
    pyautogui.click()


def click_start():
    isstarted = await_image('znaleziono2.png')
    if isstarted:
        pyautogui.moveTo(341, 75, duration=0.5)
        pyautogui.click()
    else:
        click_start()
        # possible infinite recursion is a safety measure in case of site malfunction


def click_search_engine():
    isdone = await_image('start_after.png')
    if isdone:
        pyautogui.moveTo(48, 116, duration=0.5)
        pyautogui.click()
    else:
        click_search_engine()
        # possible infinite recursion is a safety measure in case of site malfunction


def click_back_n_times():
    screen = get_screenshot_with_size(465, 51, 474, 73)     # screenshot of 'Nowe' value
    n = recognize_number(screen) + 1                    # adding one for basal 1 back click
    pyautogui.moveTo(1785, 142, duration=0.5)
    pyautogui.click(clicks=n, interval=0.5)


def check_site():
    pyautogui.moveTo(1785, 500, duration=1)
    pyautogui.scroll(7000)
    is_right_site = await_image('znaleziono2.png')
    if is_right_site:
        pass
    else:
        pyautogui.moveTo(1785, 142, duration=1)
        pyautogui.click()
        check_site()


def click_next():
    pyautogui.scroll(-7000)
    location = pyautogui.locateOnScreen('nastepna.png')
    center = pyautogui.center(location)
    pyautogui.moveTo(center[0], center[1], duration=0.5)
    pyautogui.click()


def autoparse():
    time.sleep(5)                                           # time given to switch windows after program start
    correct_scrollbar()
    click_search()

    while True:
        click_start()
        click_search_engine()
        click_back_n_times()
        check_site()
        click_next()


# todo: wrap the whole program in try - except to catch the error by ESCAPE MOVEMENT
# todo find out about imports - why red when files are in the same directory?





