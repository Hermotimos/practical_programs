#! python3
# mouseNow.py - Displays the mouse cursor's current position

import pyautogui
import time

print('Stop program in PyCharm to quit.')

while True:
    x, y = pyautogui.position()
    position_str = str(x) + ', ' + str(y)
    print(position_str, end='')
    time.sleep(0.01)
    print('\b' * len(position_str), end='', flush=True)
