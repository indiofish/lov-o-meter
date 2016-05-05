import lexer
import jpype
# Kkma is slower, yet more verbose than Mecab.
# If speed becomes the issue, consider changing to Mecab.
from konlpy.tag import Kkma
from multiprocessing import Pool
from threading import Thread
# from konlpy.tag import Mecab

nl_parser = Kkma()


def tagging(start, end, lines, result):
    jpype.attachThreadToJVM()
    for i in range(start, end):
        d = lines[i]
        result.append((d[0], d[1], nl_parser.pos(d[2])))
    return


def parse(fp):
    jpype.attachThreadToJVM()
    # to avoid error when ran as a thread
    chat = lexer.lex(fp)
    nlines = len(chat)
    ret = []
    t1 = Thread(target=tagging, args=(0, nlines//4, chat, ret))
    t2 = Thread(target=tagging, args=(nlines//4+1, nlines//2, chat, ret))
    t3 = Thread(target=tagging, args=(nlines//2+1, 3*(nlines//4), chat, ret))
    t4 = Thread(target=tagging, args=(3*(nlines//4)+1, nlines, chat, ret))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    return ret
