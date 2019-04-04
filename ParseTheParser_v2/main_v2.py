import time
import pyautogui
from movement_and_clicks_v2 import autoparse
from begin import ask_confirm


pages = ask_confirm()
time.sleep(5)
try:
    autoparse(pages)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")

