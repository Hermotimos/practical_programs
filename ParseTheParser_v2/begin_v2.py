
def ask_pages():
    confirm = input('Enter number of pages to browse and confirm by ENTER:\n')
    try:
        confirm = int(confirm)
        assert confirm > 0
        return confirm
    except Exception as e:
        print('ERROR:', e)
        return ask_pages()


def ask_correct():
    return yes_or_no('Would you like to automatically check start settings and correct if wrong (y/n) ?\n')


def ask_fullscreen():
    return yes_or_no('Would you like to switch to full screen for better reliability (y/n) ?\n')


def yes_or_no(prompt):
    answer = input(prompt)
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("Wrong value entered. Please choose again.\n")
        return yes_or_no(prompt)