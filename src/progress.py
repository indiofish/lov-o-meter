from time import sleep
from threading import Thread


class ProgressBar(object):
    """progressbar ui drawer"""
    def __init__(self, msg="Processing", full=100):
        self.done = False
        self.msg = msg
        self.progress = 0
        self.full = full

    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, done):
        if done:
            # clear screen
            print("\x1b[K", end='\r')
        self.__done = done

    def show_progress(self):
        """create a seperate thread that draws a progress bar"""
        bar = Thread(target=self.__show_progress_bars__)
        bar.daemon = True
        bar.start()

    def __show_progress_dots__(self):
        """draws 3 dots until done"""
        cnt = 0
        while not self.done:
            print("\x1b[K" + self.msg + "." * cnt, end='\r')
            cnt = (cnt + 1) % 4
            sleep(1.0)

    def __show_progress_bars__(self):
        while not self.done:
            progress = int((self.progress / self.full) * 100)
            print("\x1b[K{}".format(progress), end='\r')
            sleep(1.0)
