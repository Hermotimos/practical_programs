import os
import time


def shutdown_countdown():
    mode = ask_shutdown_mode()
    minutes = ask_time()
    ending = ''

    if minutes == 1:
        ending = 'ę'
    elif 1 < minutes < 5:
        ending = 'y'
    print('\nKomputer zostanie wyłączony za {} minut{}.'
          '\nOtwarte programy zostaną wyłączone...'
          '\nZapisz pliki przed końcem odliczania, aby uniknąć utraty danych!!!'
          '\nW każdej chwili możesz przerwać odliczanie przez wyłączenie okna programu.'
          .format(minutes, ending))

    timer_secs = minutes * 60
    while timer_secs > 0:
        """
        'minutes' are deprecated before first print, 
        cause exe file created by pyinstaller misses a minute somehow and prints this variable only after 1 min
        """
        minutes -= 1
        print('\n', str(minutes), end='')
        timer_secs -= 60
        time.sleep(60)
    os.system("{}".format(mode))


def ask_time():
    entry = input("Podaj za ile minut chcesz wyłączyć komputer i zatwierdź przez ENTER:\n")
    try:
        entry = int(entry)
        assert entry > 0
        return entry
    except Exception:
        print("Podana wartość jest błędna. Spróbuj jeszcze raz.\n")
        return ask_time()


def ask_shutdown_mode():
    entry = input("Wybierz opcję zamykania systemu:\n1 - zamknięcie \n2 - hibernacja\n")
    mode = ''
    try:
        entry = int(entry)
        assert entry in (1, 2)
        if entry == 1:
            mode = "shutdown /s /t 1"
        elif entry == 2:
            mode = "shutdown /h"
        return mode
    except Exception:
        print("Podana wartość jest błędna. Spróbuj jeszcze raz.\n")
        return ask_shutdown_mode()


shutdown_countdown()
