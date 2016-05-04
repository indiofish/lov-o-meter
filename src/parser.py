import lexer
from konlpy.tag import Kkma
from konlpy.tag import Mecab

nl_parser = Kkma()


def parse(filename):
    chat = lexer.lex(filename)
    for ln in chat:
        ret = nl_parser.pos(ln[2])
        print(ret)
