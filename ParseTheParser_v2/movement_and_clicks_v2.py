import pyautogui
import datetime
import time
from image_processing_v2 import await_image, try_click_image, recognize_number
from verify_Start import correct_settings, do_fullscreen

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True


IMG_STATUS = '.\\IMG_STATUS.png'
IMG_SZUKAJ = '.\\IMG_SZUKAJ.png'
IMG_START_BLACK = '.\\IMG_START_BLACK.png'
IMG_NASTEPNA = '.\\IMG_NASTEPNA.png'
IMG_START_GREY = '.\\IMG_START_GREY.png'
IMG_WYSZUKIWARKA = '.\\IMG_WYSZUKIWARKA.png'
IMG_BLUELINE = '.\\IMG_BLUELINE.png'
IMG_BACK = '.\\IMG_BACK.png'
IMG_LISTA = '.\\IMG_LISTA.png'


def autoparse(pages_to_browse, correction=False, fullscreen=False):
    page_cnt = 0
    new_cnt = 0

    print('-' * 20, 'START', '-' * 20)

    if correction:
        correct_settings()
    if fullscreen:
        do_fullscreen()
    start_browsing()

    while pages_to_browse > 0:
        page_cnt += 1
        pages_to_browse -= 1
        print('{}'.format(str(page_cnt)))

        click_start()
        switch_to_search_window()
        new_items = click_back_n_times()
        actively_check_list_site()
        click_next()

        new_cnt += new_items
        print('\t'*10, '+{} [SUM TOTAL: {}]'.format(new_items, new_cnt))

    finish_browsing(new_cnt)


def start_browsing():

    def scrollbar_down():
        t = time.time()
        try_click_image(IMG_STATUS)
        pyautogui.scroll(-7000)
        print('\t{}s'.format(round(time.time() - t), 0))

    def click_search():
        t = time.time()
        try_click_image(IMG_SZUKAJ)
        print('\t{}s'.format(round(time.time() - t), 0))

    scrollbar_down()
    click_search()
    print()


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