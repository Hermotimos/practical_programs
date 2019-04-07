import pyautogui
import datetime
from parse_flow import autoparse
from settings import ask_pages

pages = ask_pages()
try:
    autoparse(pages)
except pyautogui.FailSafeException:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print("\n[{}] FAILSAFE-ESCAPED.".format(now))
