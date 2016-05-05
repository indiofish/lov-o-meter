import main
import progress
import threading

th = threading.Thread(target=main.main)
p = threading.Thread(target=progress.show_progress, args=(th,))
th.start()
p.start()
