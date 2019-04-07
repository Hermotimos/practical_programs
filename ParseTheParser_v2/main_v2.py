import pyautogui
import datetime
from parse_flow import browse_pages
from settings import ask_pages

pages = ask_pages()
try:
    browse_pages(pages)
except pyautogui.FailSafeException:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print("\n[{}] FAILSAFE-ESCAPED.".format(now))
