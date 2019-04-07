import pyautogui
import datetime
from parse_flow import start_browsing, browse_pages, finish_browsing
from settings import ask_numberof_pages

pages = ask_numberof_pages()
try:
    start_browsing()
    new_sum = browse_pages(pages)
    finish_browsing(new_sum)
except pyautogui.FailSafeException:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print("\n[{}] FAILSAFE-ESCAPED.".format(now))
