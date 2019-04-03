import pyautogui
import time
from compareScreenshots import recognize_number, await_image


pyautogui.PAUSE = 0.5                   # sets pause between function calls to n secs
pyautogui.FAILSAFE = True               # possible escape by moving cursor to upper left corner of screen


def autoparse():
    # time given to switch windows after program start
    time.sleep(5)
    # set right scroll bar to uppmost position
    pyautogui.moveTo(1906, 193, duration=0)
    pyautogui.click()
    # click SEARCH
    pyautogui.moveTo(1185, 813, duration=1)
    pyautogui.click()

    while True:
        # click START
        time.sleep(2)
        isfound = await_image('found.png')
        if isfound:
            pyautogui.moveTo(341, 75, duration=2)
            pyautogui.click()


        # click SEARCH ENGINE
        # todo await_not_blank
        pyautogui.moveTo(48, 116, duration=1)
        pyautogui.click()

        # click BACK n times
        pyautogui.moveTo(1785, 142, duration=1)
        screen = pyautogui.screenshot(region=(465, 51, 474, 73))     # screenshot of 'Nowe' value
        cnt = recognize_number(screen)
        backclicks = cnt + 1
        pyautogui.click(clicks=backclicks, interval=0.5)

        # scrolldown and click next
        pyautogui.moveTo(1785, 500, duration=2)
        pyautogui.scroll(-3000)
        pyautogui.moveTo(1140, 825, duration=1)
        pyautogui.click()


# todo: wrap the whole program in try - except to catch the error by ESCAPE MOVEMENT
# todo find out about imports - why red when files are in the same directory?





