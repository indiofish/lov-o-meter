import lexer
import jpype
from datetime import datetime
from threading import Thread
# Kkma is slower, yet more verbose than Mecab.
# If speed becomes the issue, consider changing to Mecab.
from konlpy.tag import Kkma
from collections import namedtuple
from konlpy.tag import Mecab

ChatData = namedtuple('ChatData',
                      ['time',
                       'user',
                       'contents'])


class ChatParser(object):
    """docstring for ChatParser"""
    def __init__(self, tagger=Kkma, thread_cnt=4):
        self.tagger = tagger()
        self.thread_cnt = thread_cnt

    def tagging(self, result, que, bar):
        """get string from a queue and tags it"""
        # to avoid error when ran as a thread
        jpype.attachThreadToJVM()
        while 1:
            try:
                # pop operation is atomic
                tok = que.pop()
                time = datetime.strptime(tok.time,
                                         "%Y-%m-%d %H:%M")
                result[tok.pos] = ChatData(
                    time, tok.user,
                    self.tagger.pos(tok.contents))
                bar.update()
            except AttributeError as e:
                pass
            except IndexError as e:
                # when competing threads try to pop()
                break
        return

    def parse(self, fp, bar):
        """create threads to tag chatlog"""
        chat_que = lexer.lex(fp)
        ret = [None] * len(chat_que)
        bar.full = len(chat_que)
        bar.start()
        pool = [Thread(target=self.tagging, args=(ret, chat_que, bar))
                for _ in range(self.thread_cnt)]
        for t in pool:
            t.daemon = True
            t.start()
        for t in pool:
            t.join()
        bar.done = True
        # print(ret)
        return ret
