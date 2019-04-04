import pyautogui
import random
from image_processing_v2 import recognize_number, await_image, get_screenshot_with_size, try_go_to_image


pyautogui.PAUSE = 0.1                   # sets pause between function calls to n secs
pyautogui.FAILSAFE = True               # possible escape by moving cursor to upper left corner of screen


def autoparse(how_many_pages):
    scrollbar_up()
    click_search()

    while how_many_pages > 0:
        click_start()
        click_search_engine()
        click_back_n_times()
        check_site()
        click_next()
        how_many_pages -= 1

    last_done = pyautogui.screenshot()
    rand = random.random()
    last_done.save('C:\\Users\\Lukasz\\Desktop\\recent{}.jpg'.format(rand))


def scrollbar_up():
    try_go_to_image('status_for_centering.png')
    pyautogui.scroll(7000)


def click_search():
    try_go_to_image('szukaj.png')
    pyautogui.click()


def click_start():
    isstarted = await_image('start_before.png')
    if isstarted:
        try_go_to_image('start_before.png')
        pyautogui.click()
    else:
        click_next()
        click_start()
        # possible infinite recursion is a safety measure in case of site malfunction


def click_search_engine():
    isdone = await_image('start_after.png')
    if isdone:
        try_go_to_image('wyszukiwarka.png')
        pyautogui.click()
    else:
        click_search_engine()
        # possible infinite recursion is a safety measure in case of site malfunction


def click_back_n_times():
    """ Checks number at specific location (n); adds 1 due to feature's design; goes-back n+1 times"""
    screen = get_screenshot_with_size(465, 51, 474, 73)
    n = recognize_number(screen) + 1
    try_go_to_image('back.png')
    pyautogui.click(clicks=n, interval=0.5)


def check_site():
    try_go_to_image('blueline.png')                 # TODO gotoimage causes errors when no such image: add check before !!!
    pyautogui.scroll(7000)
    is_right_site = await_image('lista.png')
    if is_right_site:
        pass
    else:
        try_go_to_image('back.png')
        pyautogui.click()
        check_site()


def click_next():
    pyautogui.scroll(-7000)
    try_go_to_image('nastepna.png')
    pyautogui.click()




