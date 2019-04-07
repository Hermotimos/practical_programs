import pyautogui
import time
from image_processing_v2 import try_click_image, recognize_number

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

IMG_APPLICATION = '.\\images\\IMG_APPLICATION.png'
IMG_HOMEPAGE = '.\\images\\IMG_HOMEPAGE.png'
IMG_ZTEZA = '.\\images\\IMG_ZTEZA.png'
IMG_ZUZASAD = '.\\images\\IMG_ZUZASAD.png'
IMG_RODZAJ = '.\\images\\IMG_RODZAJ.png'
IMG_WYROK = '.\\images\\IMG_WYROK.png'
IMG_NROSTAT = '.\\images\\IMG_NROSTAT.png'

IMG_STATUS = '.\\images\\IMG_STATUS.png'
IMG_SZUKAJ = '.\\images\\IMG_SZUKAJ.png'
IMG_START_BLACK = '.\\images\\IMG_START_BLACK.png'
IMG_NASTEPNA = '.\\images\\IMG_NASTEPNA.png'
IMG_START_GREY = '.\\images\\IMG_START_GREY.png'
IMG_WYSZUKIWARKA = '.\\images\\IMG_WYSZUKIWARKA.png'
IMG_WYSZUKIWARKA_2 = '.\\images\\IMG_WYSZUKIWARKA_2.png'
IMG_BLUELINE = '.\\images\\IMG_BLUELINE.png'
IMG_BACK = '.\\images\\IMG_BACK.png'
IMG_LISTA = '.\\images\\IMG_LISTA.png'


# ELEMENTS OF start_browsing()
def determine_startpoint():
    if pyautogui.locateOnScreen(IMG_STATUS, 1):
        return True
    elif pyautogui.locateOnScreen(IMG_LISTA, 1):
        return False
    else:
        determine_startpoint()


def scrolldown_startpage():
    t = time.time()
    try_click_image(IMG_STATUS)
    pyautogui.scroll(-7000)
    print('\t{}s'.format(round(time.time() - t), 0))


def click_search():
    t = time.time()
    try_click_image(IMG_SZUKAJ)
    print('\t{}s'.format(round(time.time() - t), 0))


def set_strony():
    t = time.time()
    try_click_image(IMG_NROSTAT)
    pyautogui.move(0, 20)
    pyautogui.click()
    pyautogui.press('delete', presses=5)
    pyautogui.typewrite('1')
    print('\t{}s'.format(round(time.time() - t), 0))


# ELEMENTS of browse_pages()
def await_blueline():
    time.sleep(1)
    if pyautogui.locateOnScreen(IMG_BLUELINE, 60):
        pass
    else:
        try_click_image(IMG_BACK)

def click_start():
    t = time.time()
    if pyautogui.locateOnScreen(IMG_START_BLACK, 30):
        try_click_image(IMG_START_BLACK)
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        try_click_image(IMG_BACK)
        click_start()


def switch_to_search_window():
    t = time.time()
    if pyautogui.locateOnScreen(IMG_START_GREY, 60):
        try_click_image(IMG_WYSZUKIWARKA)
        print('\t{}s'.format(round(time.time() - t), 0))
    elif pyautogui.locateOnScreen(IMG_WYSZUKIWARKA_2, 1):
        pass
    else:
        switch_to_search_window()


def click_back_n_times():
    t = time.time()
    new = recognize_number()
    n_times = new + 1
    print('back x{}'.format(n_times))
    try_click_image(IMG_BACK, clicks=n_times, interval=0.5)
    print('\t{}s'.format(round(time.time() - t), 0))
    return new


def actively_check_list_site():                             # todo rethink this one
    t = time.time()
    if pyautogui.locateOnScreen(IMG_LISTA, 15):
        try_click_image(IMG_LISTA)
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        pyautogui.locateOnScreen(IMG_BACK)
        pyautogui.move(0, 30)
        pyautogui.scroll(7000)
        if pyautogui.locateOnScreen(IMG_LISTA, 15):
            try_click_image(IMG_LISTA)
            print('\t{}s'.format(round(time.time() - t), 0))
        else:
            try_click_image(IMG_BACK)
            actively_check_list_site()


def click_next():
    t = time.time()
    pyautogui.scroll(-7000)
    try_click_image(IMG_NASTEPNA)
    print('\t{}s'.format(round(time.time() - t), 0))


#
# def continue_browsing():
#     actively_check_list_site()
#     click_next()
#
#
# def do_fullscreen():
#     pass        # todo
