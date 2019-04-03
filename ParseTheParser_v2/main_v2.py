from movement_and_clicks_v2 import autoparse
import pyautogui
import time


def ask_confirm():
    confirm = input('\n\n!!! PREPARE YOUR PARSER !!!\n\n'
                    '1. TYPE OF SENTENCES TO BROWSE.\n'
                    '2. END DATE\n'
                    '3. SET "without thesis" AND "with justification" fields.\n'
                    '4. NUMBER OF PAGES = 1\n\n'
                    'Enter number of pages to browse or leave empty for 10000:\n'
                    'CONFIRM: ENTER ===> you will then have 5 secs to switch to the Parser window.\n')
    if confirm == '':
        confirm = 10000
    try:
        confirm = int(confirm)
        assert confirm > 0
        return confirm
    except Exception as e:
        print(e)
        return ask_confirm()


pages = ask_confirm()
time.sleep(5)
try:
    autoparse(pages)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")



# TODO change of program window size seems to change pixels in numbers data
# Sol1 - measure accuracy
# Sol2 - full screen only [add to program]
# Sol3 - look for one