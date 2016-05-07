from time import sleep
from threading import Thread


class ProgressBar(object):
    """draw a progress bar until condition is met"""
    def __init__(self, msg="Processing"):
        self.finished = False
        self.msg = msg

    @property
    def finished(self):
        return self.__finished

    @finished.setter
    def finished(self, finished):
        if finished:
            # clear screen
            print("\x1b[K", end='\r')
        self.__finished = finished

    def show_progress(self):
        bar = Thread(target=self.__show_progress_dots__)
        bar.daemon = True
        bar.start()

    def __show_progress_dots__(self):
        cnt = 0
        while not self.finished:
            print("\x1b[K" + self.msg + "." * cnt, end='\r')
            cnt = (cnt + 1) % 4
            sleep(1.0)
        # clear screen
