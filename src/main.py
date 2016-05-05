import parser
import progress
import threading

def helper(fp):
    chat = parser.parse(fp)
    return chat

def main():
    # TODO
    # call parser
    # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
    try:
        fp = open("../tests/KakaoTalkChats.txt", 'r', encoding='utf-8')
        th = threading.Thread(target=helper, args=(fp,))
        proc_bar = threading.Thread(target=progress.show_progress, args=(th,))
        th.start()
        proc_bar.start()
    except IOError:
        print("NO SUCH FILE")
if __name__ == '__main__':
    main()
