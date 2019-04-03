from movement_and_clicks import autoparse
import pyautogui


def ask_confirm():
    confirm = input('\n\n!!! REMEMBER !!!\n\n'
                    '0. FULL SCREEN\n'
                    '1. TYPE OF SENTENCES TO BROWSE.\n'
                    '2. END DATE\n'
                    '3. SET "without thesis" AND "with justification" fields.\n'
                    '4. NUMBER OF PAGES = 1\n\n'
                    'CONFIRM: Type "ok" + ENTER ===> you will have 5 secs to switch to the Parser window.\n')
    try:
        assert confirm == 'ok'
        print('TO ESCAPE: while the cursor is moving, rapidly move it to the upper left corner of the screen.\n')
    except Exception:
        return ask_confirm()


ask_confirm()
try:
    autoparse()
except pyautogui.FailSafeException:
    print("FAILSAFE-ESCAPED.")
