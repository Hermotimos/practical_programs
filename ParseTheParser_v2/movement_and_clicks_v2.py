import pyautogui
import datetime
import time
from image_processing_v2 import await_image, try_click_image, recognize_number

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

IMG_HOMEPAGE = '.\\IMG_HOMEPAGE.png'
IMG_ZTEZA = '.\\IMG_ZTEZA.png'
IMG_ZUZASAD = '.\\IMG_ZUZASAD.png'
IMG_RODZAJ = '.\\IMG_RODZAJ.png'
IMG_WYROK = '.\\IMG_WYROK.png'
IMG_NROSTAT = '.\\IMG_NROSTAT.png'

IMG_STATUS = '.\\IMG_STATUS.png'
IMG_SZUKAJ = '.\\IMG_SZUKAJ.png'
IMG_START_BLACK = '.\\IMG_START_BLACK.png'
IMG_NASTEPNA = '.\\IMG_NASTEPNA.png'
IMG_START_GREY = '.\\IMG_START_GREY.png'
IMG_WYSZUKIWARKA = '.\\IMG_WYSZUKIWARKA.png'
IMG_BLUELINE = '.\\IMG_BLUELINE.png'
IMG_BACK = '.\\IMG_BACK.png'
IMG_LISTA = '.\\IMG_LISTA.png'


def click_start():
    t = time.time()
    is_start_black_visible = await_image(IMG_START_BLACK, 30)
    if is_start_black_visible:
        try_click_image(IMG_START_BLACK)
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        click_next()
        click_start()


def switch_to_search_window():
    t = time.time()
    is_start_grey_visible = await_image(IMG_START_GREY, 60)
    if is_start_grey_visible:
        try_click_image(IMG_WYSZUKIWARKA)
        print('\t{}s'.format(round(time.time() - t), 0))
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


def actively_check_list_site():
    t = time.time()
    is_lista_visible = await_image(IMG_LISTA, 5)

    if is_lista_visible:
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


def correct_settings():

    def correct_homepage():
        t = time.time()
        try_click_image(IMG_HOMEPAGE)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - t), 0))

    def correct_zteza():
        t = time.time()
        is_zteza_none = await_image(IMG_ZTEZA, 1)
        if is_zteza_none:
            try_click_image(IMG_ZTEZA)
            pyautogui.move(90, 0)
            pyautogui.click()
            print('\t{}s'.format(round(time.time() - t), 0))

    def correct_zuzasad():
        t = time.time()
        is_zuzasad_none = await_image(IMG_ZUZASAD, 1)
        if is_zuzasad_none:
            try_click_image(IMG_ZUZASAD)
            pyautogui.move(30, 0)
            pyautogui.click()
            print('\t{}s'.format(round(time.time() - t), 0))

    def correct_rodzaj():
        t = time.time()
        is_rodzaj_none = await_image(IMG_RODZAJ, 1)
        if is_rodzaj_none:
            try_click_image(IMG_RODZAJ)
            pyautogui.click()
            try_click_image(IMG_WYROK)
            pyautogui.click()
            print('\t{}s'.format(round(time.time() - t), 0))

    def correct_nrostat():
        t = time.time()
        try_click_image(IMG_NROSTAT)
        pyautogui.move(0, 20)
        pyautogui.click()
        pyautogui.press('delete', presses=5)
        pyautogui.typewrite('1')
        print('\t{}s'.format(round(time.time() - t), 0))

    correct_homepage()
    correct_zteza()
    correct_zuzasad()
    correct_rodzaj()
    correct_nrostat()


def do_fullscreen():
    pass        # todo
