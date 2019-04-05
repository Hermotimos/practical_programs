import pyautogui
from movement_and_clicks_v2 import autoparse
from begin_v2 import ask_pages

pages = ask_pages()
try:
    autoparse(pages)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
