from time import sleep
from itertools import cycle
progress = cycle(('ㅡ', '\\', '|', '/',))


def show_progress(th):
    while th.is_alive():
        print("Processing... "+ next(progress), end='\r')
        sleep(0.5)
