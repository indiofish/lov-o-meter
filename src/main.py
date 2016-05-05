import parser
import queue
import progress
import threading

def helper(filename, queue):
    # TODO
    # call parser
    # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
    with open(filename, 'r', encoding='utf-8') as fp:
        chat = parser.parse(fp)
    queue.put(chat)
    return


def main():
    que = queue.Queue()
    filename = "../tests/KakaoTalkChats.txt"
    try:
        th = threading.Thread(target=helper, args=(filename, que))
        proc_bar = threading.Thread(target=progress.show_progress, args=(th,))
        th.start()  # start processing file data
        proc_bar.start()  # draw process bar for user
        th.join()
        result = que.get()  # get result of helper function
        print(result)
    except IOError:
        print("NO SUCH FILE")

if __name__ == '__main__':
    main()
