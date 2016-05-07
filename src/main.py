import parser
import stats
import analyser
from progress import ProgressBar


def helper(filename):
    # TODO
    # call parser # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
    with open(filename, 'r', encoding='utf-8') as fp:
        chat = parser.parse(fp)
    chatdata = stats.get_stats(chat)
    ret = analyser.analyse(chatdata)
    return ret


def main():
    filename = "../tests/KakaoTalkChats.txt"
    bar = ProgressBar()
    bar.show_progress()
    try:
        result = helper(filename)
    except IOError:
        bar.done = True
        print("NO SUCH FILE")
    bar.done = True
    print(result)

if __name__ == '__main__':
    main()
