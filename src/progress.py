from time import sleep


def show_progress(th):
    cnt = 0
    while th.is_alive():
        print("\x1b[KProcessing" + "." * cnt, end='\r')
        cnt = (cnt + 1) % 4
        sleep(0.5)
