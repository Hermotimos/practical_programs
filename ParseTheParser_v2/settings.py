
def ask_pages():
    confirm = input('Enter number of pages to browse and confirm by ENTER:\n')
    try:
        confirm = int(confirm)
        assert confirm > 0
        return confirm
    except Exception as e:
        print('ERROR:', e)
        return ask_pages()


def yes_or_no(prompt):
    answer = input(prompt)
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("Wrong value entered. Please choose again.\n")
        return yes_or_no(prompt)


# todo: ask if start from start page or continue from current site?