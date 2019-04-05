import pyautogui
from movement_and_clicks_v2 import autoparse
from begin_v2 import ask_pages, ask_correct, ask_fullscreen

pages = ask_pages()
if_correct = ask_correct()
if_fullscreen = ask_fullscreen()
try:
    autoparse(pages, if_correct, if_fullscreen)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
