from movement_and_clicks_v2 import autoparse
import pyautogui


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
        int(confirm)
        assert confirm > 0
        return confirm
    except Exception:
        return ask_confirm()


pages = ask_confirm()
try:
    autoparse(pages)
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
