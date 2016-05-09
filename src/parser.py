import lexer
import jpype
# Kkma is slower, yet more verbose than Mecab.
# If speed becomes the issue, consider changing to Mecab.
from konlpy.tag import Kkma
from threading import Thread
# from konlpy.tag import Mecab


class ChatParser(object):
    """docstring for ChatParser"""
    def __init__(self):
        self.tagger = Kkma()
        self.thread_cnt = 4

    def tagging(self, result, que):
        """get string from a queue and tags it"""
        # to avoid error when ran as a thread
        jpype.attachThreadToJVM()
        while 1:
            try:
                tok = que.pop()
                result[tok.pos] = (tok.time, tok.user,
                                   self.tagger.pos(tok.contents))
            except AttributeError:
                pass
            except IndexError:
                break
        return

    def parse(self, fp, bar):
        """create threads to tag chatlog using a thread-safe queue"""
        chat_len, chat_que = lexer.lex(fp)
        ret = [None] * chat_len
        bar.show_progress()
        pool = [Thread(target=self.tagging, args=(ret, chat_que))
                for _ in range(self.thread_cnt)]
        for t in pool:
            t.daemon = True
            t.start()
        # while len(chat_que):
            # progress = int(((chat_len-len(chat_que)) / chat_len)*100)
            # bar.progress = progress
        for t in pool:
            t.join()

        bar.done = True
        # print(ret)
        return ret
