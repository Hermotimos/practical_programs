import pyautogui
from parse_flow import autoparse
from settings import ask_pages

pages = ask_pages()
try:
    autoparse(pages)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
