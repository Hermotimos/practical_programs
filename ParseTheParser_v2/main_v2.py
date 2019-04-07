import pyautogui
from parse_flow import autoparse
from settings import ask_pages, ask_default_start, ask_fullscreen

pages = ask_pages()
if_default = ask_default_start()
if_fullscreen = ask_fullscreen()
try:
    autoparse(pages, if_default, if_fullscreen)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
