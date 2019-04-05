import pyautogui
import datetime
import time
from image_processing_v2 import try_recognize_number, await_image, try_go_to_image

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


def autoparse(how_many_pages, counter_pages=1):
    print('-' * 20, 'START', '-' * 20)
    counter_new = 0
    correct_settings()
    start_browsing()

    while how_many_pages > 0:
        print('{}'.format(str(counter_pages)))

        click_start()
        click_search_engine()
        new_items = click_back_n_times()
        actively_check_blueline()
        actively_check_list_site()
        click_next()

        how_many_pages -= 1
        counter_pages += 1
        counter_new += new_items
        print('\t'*10, '+{}'.format(counter_new))
        print('\t'*12, 'SUM TOTAL:\t{}'.format(counter_new))

    finish_browsing(counter_new)


def correct_settings():

    def correct_homepage():
        t = time.time()
        try_go_to_image(IMG_HOMEPAGE)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - t), 0))

    def correct_zteza():
        t = time.time()
        is_zteza_none = await_image(IMG_ZTEZA, 1)
        if is_zteza_none:
            try_go_to_image(IMG_ZTEZA)
            pyautogui.move(90, 0)
            pyautogui.click()
            print('\t{}s'.format(round(time.time() - t), 0))

    def correct_zuzasad():
        t = time.time()
        is_zuzasad_none = await_image(IMG_ZUZASAD, 1)
        if is_zuzasad_none:
            try_go_to_image(IMG_ZUZASAD)
            pyautogui.move(30, 0)
            pyautogui.click()
            print('\t{}s'.format(round(time.time() - t), 0))

    def correct_rodzaj():
        t = time.time()
        is_rodzaj_none = await_image(IMG_RODZAJ, 1)
        if is_rodzaj_none:
            try_go_to_image(IMG_RODZAJ)
            pyautogui.click()
            try_go_to_image(IMG_WYROK)
            pyautogui.click()
            print('\t{}s'.format(round(time.time() - t), 0))

    def correct_nrostat():
        t = time.time()
        try_go_to_image(IMG_NROSTAT)
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


def start_browsing():

    def scrollbar_down():
        t = time.time()
        try_go_to_image(IMG_STATUS)
        pyautogui.click()
        pyautogui.scroll(-7000)
        print('\t{}s'.format(round(time.time() - t), 0))

    def click_search():
        t = time.time()
        try_go_to_image(IMG_SZUKAJ)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - t), 0))

    scrollbar_down()
    click_search()
    print()


def click_start():
    t = time.time()
    is_start_black_visible = await_image(IMG_START_BLACK, 30)
    if is_start_black_visible:
        try_go_to_image(IMG_START_BLACK)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        click_next()
        click_start()


def click_next():
    t = time.time()
    pyautogui.scroll(-7000)
    try_go_to_image(IMG_NASTEPNA)
    pyautogui.click()
    print('\t{}s'.format(round(time.time() - t), 0))


def click_search_engine():
    t = time.time()
    is_start_grey_visible = await_image(IMG_START_GREY)
    if is_start_grey_visible:
        try_go_to_image(IMG_WYSZUKIWARKA)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        click_search_engine()


def click_back_n_times():
    t = time.time()
    new = try_recognize_number()
    n_times = new + 1
    print('IMG_BACK: x{}'.format(n_times))
    try_go_to_image(IMG_BACK)
    pyautogui.click(clicks=n_times, interval=0.5)
    print('\t{}s'.format(round(time.time() - t), 0))
    return new


def actively_check_blueline():
    t = time.time()
    isblueline_visible = await_image(IMG_BLUELINE, 10)

    if isblueline_visible:
        try_go_to_image(IMG_BLUELINE)
        pyautogui.scroll(7000)
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        try_go_to_image(IMG_BACK)
        pyautogui.click()
        actively_check_blueline()


def actively_check_list_site():
    t = time.time()
    is_lista_visible = await_image(IMG_LISTA, 5)

    if is_lista_visible:
        try_go_to_image(IMG_LISTA)
        print('\t{}s'.format(round(time.time() - t), 0))
    else:
        try_go_to_image(IMG_BACK)
        pyautogui.click()
        actively_check_list_site()


def finish_browsing(new_items):
    def now_str():
        now = datetime.datetime.now()
        return now.strftime('%H.%M')

    def save_screenshot():
        last_page = pyautogui.screenshot()
        last_page.save('C:\\Users\\Lukasz\\Desktop\\recent__{}.jpg'.format(now_str()))

    save_screenshot()
    print('-'*20, 'END', '-'*20, '\nFinished: {}\nNew: {}'.format(now_str(), new_items))
