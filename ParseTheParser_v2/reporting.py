import os


def check_directory():
    folder = '.\\reports'
    if folder not in os.listdir('.'):
        os.mkdir(folder)

def write_report():
    check_directory()
