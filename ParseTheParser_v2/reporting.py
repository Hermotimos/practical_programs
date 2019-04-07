import os
import datetime
from movement_and_clicks_v2 import click_next


def report(called_function):
    print('[{}] '.format(datetime.datetime.now().strftime('%H:%M:%S')), end='')
    print(called_function.__repr__().split()[1])
    called_function()

# it works, but causes problems if called function calls other functions
# but maybe only because the ones called stll have older reporting from within...


report(click_next)


