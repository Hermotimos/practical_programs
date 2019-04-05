import pyautogui
import datetime
import time
from image_processing_v2 import try_recognize_number, await_image, try_go_to_image

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

status_button = '.\\status_button.png'
szukaj = '.\\szukaj.png'
start_black = '.\\start_black.png'
nastepna = '.\\nastepna.png'
start_grey = '.\\start_grey.png'
wyszukiwarka = '.\\wyszukiwarka.png'
blueline = '.\\blueline.png'
back = '.\\back.png'
lista = '.\\lista.png'


def autoparse(how_many_pages, counter_pages=1):
    counter_new = 0
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
        print('\t'*12, 'TOTAL:\t{}'.format(counter_new))

    finish_browsing(counter_new)


def start_browsing():
    def scrollbar_down():
        timer = time.time()
        try_go_to_image(status_button)
        pyautogui.click()
        pyautogui.scroll(-7000)
        print('\t{}s'.format(round(time.time() - timer), 0))

    def click_search():
        timer = time.time()
        try_go_to_image(szukaj)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - timer), 0))

    print('-'*20, 'START', '-'*20)
    scrollbar_down()
    click_search()
    print()


def click_start():
    timer = time.time()
    is_start_black_visible = await_image(start_black, 30)
    if is_start_black_visible:
        try_go_to_image(start_black)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - timer), 0))
    else:
        click_next()
        click_start()


def click_next():
    timer = time.time()
    pyautogui.scroll(-7000)
    try_go_to_image(nastepna)
    pyautogui.click()
    print('\t{}s'.format(round(time.time() - timer), 0))


def click_search_engine():
    timer = time.time()
    is_start_grey_visible = await_image(start_grey)
    if is_start_grey_visible:
        try_go_to_image(wyszukiwarka)
        pyautogui.click()
        print('\t{}s'.format(round(time.time() - timer), 0))
    else:
        click_search_engine()


def click_back_n_times():
    timer = time.time()
    new = try_recognize_number()
    n_times = new + 1
    print('back: x{}'.format(n_times))
    try_go_to_image(back)
    pyautogui.click(clicks=n_times, interval=0.5)
    print('\t{}s'.format(round(time.time() - timer), 0))
    return new


def actively_check_blueline():
    timer = time.time()
    isblueline_visible = await_image(blueline, 10)
    if isblueline_visible:
        try_go_to_image(blueline)
        pyautogui.scroll(7000)
        print('\t{}s'.format(round(time.time() - timer), 0))
    else:
        try_go_to_image(back)
        pyautogui.click()
        actively_check_blueline()


def actively_check_list_site():
    timer = time.time()
    is_lista_visible = await_image(lista, 5)
    if is_lista_visible:
        try_go_to_image(lista)
        print('\t{}s'.format(round(time.time() - timer), 0))
    else:
        try_go_to_image(back)
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
