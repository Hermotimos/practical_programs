import time
import pyautogui
from image_processing_v2 import try_click_image, await_image

IMG_HOMEPAGE = '.\\IMG_HOMEPAGE.png'
IMG_ZTEZA = '.\\IMG_ZTEZA.png'
IMG_ZUZASAD = '.\\IMG_ZUZASAD.png'
IMG_RODZAJ = '.\\IMG_RODZAJ.png'
IMG_WYROK = '.\\IMG_WYROK.png'
IMG_NROSTAT = '.\\IMG_NROSTAT.png'


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