from movement_and_clicks_v2 import *


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
        print('\t' * 10, '+{} [SUM TOTAL: {}]'.format(new_per_page, new_count))
    return new_count


start_browsing()

new_sum = browse_pages(4)

finish_browsing(new_sum)



