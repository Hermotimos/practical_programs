import os
import pyautogui
import datetime
from parse_flow import start_browsing, browse_pages, finish_browsing
from settings import ask_number_pages, ask_shutdown


def main_flow(pages_to_browse, shutdown_mode):
    num_pages = pages_to_browse
    ifshut = shutdown_mode
    try:
        start_browsing()
        new_sum = browse_pages(num_pages)
        finish_browsing(new_sum)
        os.system("{}".format(ifshut))
    except RecursionError:
        print('PROGRAM RECALIBRATION')
        main_flow(num_pages, ifshut)
    except pyautogui.FailSafeException:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print('\n[{}] FAILSAFE-ESCAPED.'.format(now))


pages = ask_number_pages()
ifshut = ask_shutdown()
main_flow(pages, ifshut)
