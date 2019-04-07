from movement_and_clicks_v2 import *


def start_browsing():
    set_strony()
    scrolldown_startpage()
    click_search()
    print()


def browse_one_page():
        actively_check_list_site()
        click_start()
        switch_to_search_window()
        new_items = click_back_n_times()
        actively_check_list_site()
        click_next()
        return new_items


def browse_pages(pages_to_browse):
    new_count = 0
    pages_browsed = 0

    while pages_to_browse > 0:
        pages_browsed += 1
        print('{}'.format(str(pages_browsed)))

        new_per_page = browse_one_page()
        new_count += new_per_page

        pages_to_browse -= 1
        print('\t' * 15, '+{}/[{}]'.format(new_per_page, new_count))
    return new_count


def finish_browsing(new_items):
    now = datetime.datetime.now().strftime('%H.%M')
    last_page = pyautogui.screenshot()
    last_page.save('C:\\Users\\Lukasz\\Desktop\\recent__{}.jpg'.format(now))
    print('-'*20, 'END', '-'*20, '\nFinished: {}\nNew: {}'.format(now, new_items))