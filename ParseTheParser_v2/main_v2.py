import pyautogui
from parse_flow import autoparse
from settings import ask_pages, ask_correct, ask_fullscreen

pages = ask_pages()
if_correct = ask_correct()
if_fullscreen = ask_fullscreen()
try:
    autoparse(pages, if_correct, if_fullscreen)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
