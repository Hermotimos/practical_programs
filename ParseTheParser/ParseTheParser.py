import pyautogui
import time

pyautogui.PAUSE = 0.5                   # sets pause between function calls to n secs
pyautogui.FAILSAFE = True               # possible escape by moving cursor to upper left corner of screen


print('1. Choose type of sentence to browse.\n'
      '2. Set end date\n'
      '3. Set "without thesis" and "with justification" fields.\n'
      '4. Set number of pages to 1\n\n'
      'QUIT: when the program starts, rapidly move the cursor to the upper left corner of the screen.')

# time given to switch windows after program start + set scroll bar to uppmost position
time.sleep(5)
pyautogui.moveTo(1906, 193, duration=0)
pyautogui.click()

# SZUKAJ
pyautogui.moveTo(1185, 813, duration=1)     # after 5 secs from start moves cursor to 'SZUKAJ'
pyautogui.click()


while True:
    # START
    pyautogui.moveTo(341, 75, duration=5)
    pyautogui.click()
    time.sleep(5)          #todo change to 20 in the final version

    # Wyszikuwarka
    pyautogui.moveTo(48, 116, duration=1)
    pyautogui.click()

    # BACK
    pyautogui.moveTo(1785, 142, duration=1)
    new_count = 1   # todo function to determine this based on image recognition

    image = pyautogui.screenshot()

    pyautogui.click(clicks=new_count, interval=0.5)

    # scrolldown and click next
    pyautogui.moveTo(1785, 500, duration=2)
    pyautogui.scroll(-3000)
    pyautogui.moveTo(1140, 825, duration=1)
    pyautogui.click()

