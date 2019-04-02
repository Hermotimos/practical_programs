import pyautogui
import time
from compareScreenshots import recognize_number


pyautogui.PAUSE = 0.5                   # sets pause between function calls to n secs
pyautogui.FAILSAFE = True               # possible escape by moving cursor to upper left corner of screen


def ask_confirm():
    confirm = input('!!! Before you start !!!\n'
                    '- full screen\n\n'
                    '1. Choose type of sentence to browse.\n'
                    '2. Set end date\n'
                    '3. Set "without thesis" and "with justification" fields.\n'
                    '4. Set number of pages to 1\n\n'
                    'QUIT: when the program starts, rapidly move the cursor to the upper left corner of the screen.\n'
                    'CONFIRM: "ok" + ENTER ===> you will have 5 secs to go to the Parser window.\n')
    try:
        if confirm == 'ok':
            pass
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

