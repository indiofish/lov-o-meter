import parser
import stats
import analyser
import progress
import threading
import queue


def helper(filename, queue):
    # TODO
    # call parser
    # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
    with open(filename, 'r', encoding='utf-8') as fp:
        chat = parser.parse(fp)
    chatdata = stats.get_stats(chat)
    ret = analyser.analyse(chatdata)
    queue.put(ret)
    return


def main():
    que = queue.Queue()
    filename = "../tests/KakaoTalkChats.txt"
    try:
        th = threading.Thread(target=helper, args=(filename, que))
        th.start()  # start processing file data
    except IOError:
        print("NO SUCH FILE")
    proc_bar = threading.Thread(target=progress.show_progress, args=(th,))
    proc_bar.start()  # draw process bar for user
    th.join()
    proc_bar.join()
    result = que.get()  # get result of helper function
    print("\x1b[K", end='\r')
    print(result)

if __name__ == '__main__':
    main()
