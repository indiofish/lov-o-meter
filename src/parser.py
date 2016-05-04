import lexer
# Kkma is slower, yet more verbose than Mecab.
# If speed becomes the issue, consider changing to Mecab.
from konlpy.tag import Kkma
# from konlpy.tag import Mecab

nl_parser = Kkma()


def parse(fp):
    chat = lexer.lex(fp)
    ret = []
    for data in chat:
        ret.append((data[0], data[1], nl_parser.pos(data[2])))
    return ret
