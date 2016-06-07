#!/usr/bin/python3
import sys
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
    print(chatdata)
    ret = stats.get_stats(chatdata)
    return ret


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("NEED FILENAME AS ARGUMENT")
        return
    bar = ProgressBar()
    try:
        result = helper(filename, bar)
    except IOError:
        print("NO SUCH FILE")
        return
    print(result)

if __name__ == '__main__':
    main()
