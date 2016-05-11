from time import sleep
from threading import Thread

HIDE_CURSOR = '\x1b[?25l'
SHOW_CURSOR = '\x1b[?25h'
CLEAR_LINE = '\x1b[K'


class ProgressBar(object):
    """progressbar ui drawer"""
    def __init__(self, msg="Processing", full=100):
        self.done = False
        self.msg = msg
        self.progress = 0
        self.full = full
        self.bar = None

    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, done):
        self.__done = done
        if done:
            self.bar.join()
            # clear screen
            print(SHOW_CURSOR+CLEAR_LINE, end='\r')

    def start(self):
        """create a seperate thread that draws a progress bar"""
        self.bar = Thread(target=self.__show_progress_bars__)
        self.bar.daemon = True
        self.bar.start()

    def __show_progress_dots__(self):
        """draws 3 dots until done"""
        cnt = 0
        while not self.done:
            print(CLEAR_LINE + self.msg + "." * cnt, end='\r')
            cnt = (cnt + 1) % 4
            sleep(1.0)

    def __show_progress_bars__(self):
        """draws filling bars until done"""
        max_bar = 40
        fill_char = '|'
        while not self.done:
            progress = (self.progress / self.full)
            bar = ("[" +
                   (fill_char*int(max_bar * progress)).ljust(max_bar) +
                   "]")
            print(HIDE_CURSOR+CLEAR_LINE+self.msg, bar, end='\r')
            sleep(0.5)
