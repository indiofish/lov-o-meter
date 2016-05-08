import parser
import stats
import analyser
from progress import ProgressBar


def helper(filename):
    """parse file, get data, and evaluate rank"""
    chat_parser = parser.ChatParser()
    with open(filename, 'r', encoding='utf-8') as fp:
        chat = chat_parser.parse(fp)
    chatdata = stats.get_stats(chat)
    ret = analyser.analyse(chatdata)
    return ret


def main():
    filename = "../tests/KakaoTalkChats1.txt"
    bar = ProgressBar()
    bar.show_progress()
    try:
        result = helper(filename)
    except IOError:
        bar.done = True
        print("NO SUCH FILE")
        return
    bar.done = True
    print(result)

if __name__ == '__main__':
    main()
