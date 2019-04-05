def ask_pages():
    confirm = input('\n!!! PREPARE YOUR PARSER !!!\n\n'
                    '1. CHOSE TYPE OF SENTENCES TO BROWSE.\n'
                    '2. SET END DATE\n'
                    '3. SET "without thesis" AND "with justification" fields.\n'
                    '4. SET NUMBER OF LAST PAGE = 1\n\n'
                    'Enter number of pages to browse and confirm by ENTER:\n')
    try:
        confirm = int(confirm)
        assert confirm > 0
        return confirm
    except Exception as e:
        print('ERROR:', e)
        return ask_pages()
