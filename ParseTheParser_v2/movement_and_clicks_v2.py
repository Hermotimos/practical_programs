import pyautogui
import datetime
from image_processing_v2 import try_recognize_number, await_image, get_screenshot_with_size, go_to_image, \
    try_go_to_image

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


def autoparse(how_many_pages):
    scrollbar_down()
    click_search()

    while how_many_pages > 0:
        click_start()
        click_search_engine()
        click_back_n_times()
        check_site()
        click_next()
        how_many_pages -= 1
    finish()


def scrollbar_down():
    try_go_to_image(status_button)
    pyautogui.scroll(-7000)


def click_search():
    try_go_to_image(szukaj)
    pyautogui.click()


def click_start():
    isstarted = await_image(start_before, 30)
    if isstarted:
        go_to_image(start_before)
        pyautogui.click()
    else:
        click_next()
        click_start()


def click_next():
    pyautogui.scroll(-7000)
    try_go_to_image(nastepna)
    pyautogui.click()


def click_search_engine():
    isdone = await_image(start_after)
    if isdone:
        go_to_image(wyszukiwarka)
        pyautogui.click()
    else:
        click_search_engine()


def click_back_n_times():
    """ Checks number at specific location (n); adds 1 due to feature's design; goes-back n+1 times"""
    screen = get_screenshot_with_size(465, 51, 474, 73)
    n = try_recognize_number(screen) + 1
    try_go_to_image(back)
    pyautogui.click(clicks=n, interval=0.5)


def check_site():
    isblueline_visible = await_image(blueline, 10)
    if isblueline_visible:
        go_to_image(blueline)
        pyautogui.scroll(7000)
    else:
        try_go_to_image(back)
        pyautogui.click()
        check_site()

    is_lista_visible = await_image(lista, 5)
    if is_lista_visible:
        pass
    else:
        try_go_to_image(back)
        pyautogui.click()
        check_site()


def finish():
    last_done = pyautogui.screenshot()
    now = datetime.datetime.now()
    now_str = str(now).replace(':', '_')
    last_done.save('C:\\Users\\Lukasz\\Desktop\\recent__{}.jpg'.format(now_str))
    print("Finished: {}".format(now))


