import pyautogui
import datetime
import time
from image_processing_v2 import try_click_image, recognize_number

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

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


def start_browsing():

    def set_strony():
        t = time.time()
        try_click_image(IMG_NROSTAT)
        pyautogui.move(0, 20)
        pyautogui.click()
        pyautogui.press('delete', presses=5)
        pyautogui.typewrite('1')
        print('\t{}s'.format(round(time.time() - t), 0))

    def scrolldown_startpage():
        t = time.time()
        try_click_image(IMG_STATUS)
        pyautogui.scroll(-7000)
        print('\t{}s'.format(round(time.time() - t), 0))

    def click_search():
        t = time.time()
        try_click_image(IMG_SZUKAJ)
        print('\t{}s'.format(round(time.time() - t), 0))

    set_strony()
    scrolldown_startpage()
    click_search()
    print()






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


def finish_browsing(new_items):
    def now_str():
        now = datetime.datetime.now()
        return now.strftime('%H.%M')

    def save_screenshot():
        last_page = pyautogui.screenshot()
        last_page.save('C:\\Users\\Lukasz\\Desktop\\recent__{}.jpg'.format(now_str()))

    save_screenshot()
    print('-'*20, 'END', '-'*20, '\nFinished: {}\nNew: {}'.format(now_str(), new_items))


def continue_browsing():
    actively_check_list_site()
    click_next()


def do_fullscreen():
    pass        # todo
