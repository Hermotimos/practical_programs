import pyautogui
import time
from compareScreenshots import recognize_number


pyautogui.PAUSE = 0.5                   # sets pause between function calls to n secs
pyautogui.FAILSAFE = True               # possible escape by moving cursor to upper left corner of screen


def ask_confirm():
    confirm = input('\n\n!!! REMEMBER !!!\n\n'
                    '0. FULL SCREEN\n'
                    '1. TYPE OF SENTENCES TO BROWSE.\n'
                    '2. END DATE\n'
                    '3. SET "without thesis" AND "with justification" fields.\n'
                    '4. NUMBER OF PAGES = 1\n\n'
                    'CONFIRM: Type "ok" + ENTER ===> you will have 5 secs to switch to the Parser window.\n')
    try:
        assert confirm == 'ok'
        print('TO ESCAPE: while the cursor is moving, rapidly move it to the upper left corner of the screen.\n')
    except Exception:
        return ask_confirm()


# time given to switch windows after program start + set scroll bar to uppmost position
ask_confirm()
time.sleep(5)
pyautogui.moveTo(1906, 193, duration=0)
pyautogui.click()

# SZUKAJ
pyautogui.moveTo(1185, 813, duration=1)
pyautogui.click()


while True:
    # START
    pyautogui.moveTo(341, 75, duration=5)
    pyautogui.click()
    time.sleep(20)

    # Wyszukiwarka
    pyautogui.moveTo(48, 116, duration=1)
    pyautogui.click()

    # BACK
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