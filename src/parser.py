import lexer
import jpype
# Kkma is slower, yet more verbose than Mecab.
# If speed becomes the issue, consider changing to Mecab.
from konlpy.tag import Kkma
from threading import Thread
# from konlpy.tag import Mecab

nl_parser = Kkma()


def tagging(start, end, lines, result):
    jpype.attachThreadToJVM()
    for i in range(start, end):
        d = lines[i]
        result[i] = (d[0], d[1], nl_parser.pos(d[2]))
    return


def parse(fp):
    # to avoid error when ran as a thread
    jpype.attachThreadToJVM()
    chat = lexer.lex(fp)
    nlines = len(chat)
    ret = [0] * nlines
    partition = nlines // 4
    pool = [Thread(target=tagging,
                   args=(partition * x, partition * (x+1), chat, ret))
            for x in range(4)]
    for t in pool:
        t.daemon = True
        t.start()
    for t in pool:
        t.join()
    print(ret)
    return ret
