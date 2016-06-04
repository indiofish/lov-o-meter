#!/usr/bin/python3
import parser
import stats
from analysis import analyser
from progress import ProgressBar


def helper(filename, bar):
    """parse file, get data, and evaluate rank"""
    chat_parser = parser.ChatParser()
    tmp = analyser.Analyser()
    with open(filename, 'r', encoding='utf-8') as fp:
        chat = chat_parser.parse(fp, bar)
    chatdata = tmp.analyse(chat)
    ret = stats.get_stats(chatdata)
    return ret


def main():
    filename = "../tests/KakaoTalkChats.txt"
    bar = ProgressBar()
    try:
        result = helper(filename, bar)
    except IOError:
        print("NO SUCH FILE")
        return
    print(result)

if __name__ == '__main__':
    main()
