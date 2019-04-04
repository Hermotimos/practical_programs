
def ask_confirm():
    confirm = input('\n\n!!! PREPARE YOUR PARSER !!!\n\n'
                    '1. CHOSE TYPE OF SENTENCES TO BROWSE.\n'
                    '2. SET END DATE\n'
                    '3. SET "without thesis" AND "with justification" fields.\n'
                    '4. SET NUMBER OF LAST PAGE = 1\n\n'
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
