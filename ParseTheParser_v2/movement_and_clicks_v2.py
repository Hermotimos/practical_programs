import pyautogui
import datetime
import time
from image_processing_v2 import try_recognize_number, await_image, try_go_to_image

status_button = '.\\status_button.png'
szukaj = '.\\szukaj.png'
start_before = '.\\start_before.png'
nastepna = '.\\nastepna.png'
start_after = '.\\start_after.png'
wyszukiwarka = '.\\wyszukiwarka.png'
blueline = '.\\blueline.png'
back = '.\\back.png'
lista = '.\\lista.png'


pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True


def autoparse(how_many_pages, counter_pages=1):
    counter_new = 0

    scrollbar_down()
    click_search()

    while how_many_pages > 0:
        print('{}'.format(str(counter_pages)))
        click_start()
        click_search_engine()
        new_items = click_back_n_times()
        check_site()
        click_next()

        how_many_pages -= 1
        counter_pages += 1
        counter_new += new_items
        print('\t'*15, '+{}'.format(counter_new))
    finish(counter_new)


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


def click_start():
    timer = time.time()
    isstarted = await_image(start_before, 30)
    if isstarted:
        try_go_to_image(start_before)
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
    isdone = await_image(start_after)
    if isdone:
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


def check_site():
    timer = time.time()
    isblueline_visible = await_image(blueline, 10)
    if isblueline_visible:
        try_go_to_image(blueline)
        pyautogui.scroll(7000)
        print('\t{}s'.format(round(time.time() - timer), 0))
    else:
        try_go_to_image(back)
        pyautogui.click()
        check_site()

    timer = time.time()
    is_lista_visible = await_image(lista, 5)
    if is_lista_visible:
        try_go_to_image(lista)
        print('\t{}s'.format(round(time.time() - timer), 0))
    else:
        try_go_to_image(back)
        pyautogui.click()
        check_site()


def finish(new_items):
    last_done = pyautogui.screenshot()
    now = datetime.datetime.now()
    now_str = str(now).replace(':', '_')
    last_done.save('C:\\Users\\Lukasz\\Desktop\\recent__{}.jpg'.format(now_str))
    print("Finished: {}\nNew: {}".format(now, new_items))


