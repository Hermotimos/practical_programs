from movement_and_clicks_v2 import *


def autoparse(pages_to_browse):
    page_cnt = 0
    new_cnt = 0

    start_browsing()

    while pages_to_browse > 0:
        page_cnt += 1
        pages_to_browse -= 1
        print('{}'.format(str(page_cnt)))

        actively_check_list_site()
        click_start()
        switch_to_search_window()
        new_items = click_back_n_times()
        actively_check_list_site()
        click_next()

        new_cnt += new_items
        print('\t'*10, '+{} [SUM TOTAL: {}]'.format(new_items, new_cnt))

    finish_browsing(new_cnt)



