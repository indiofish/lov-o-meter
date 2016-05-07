# break text log in to meaningful parts
import datetime
import re
import queue
from collections import namedtuple

KAKAO = "카카오톡"
PM = "오후"
ME = 1
OTHER = 0
ChatToken = namedtuple('ChatToken',
                       ['pos', 'time', 'user', 'contents'])


def lex(fp):
    header = fp.readline()
    if KAKAO in header:
        # consume extra line
        fp.readline()
        ret = __kakao_lexer__(fp)
        return ret
    else:
        raise IOError


def __kakao_lexer__(f):
    pattern = ("(\d+)년 (\d+)월 (\d+)일 " +  # y/m/d
               "(\w+) (\d+):(\d+), " +  # am|pm /h/m
               "(\w+) : (.*)")  # name/contents
    regex = re.compile(pattern)
    que = queue.Queue()
    idx = 0

    for ln in f:
        match = re.search(regex, ln)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            hour = int(match.group(5))
            minute = int(match.group(6))
            user = match.group(7)
            contents = match.group(8)

            if match.group(4) == PM:
                # if not 12:??, add 12
                hour += 12 * (hour != 12)
            user = int(match.group(7) == "회원님")
            time = datetime.datetime(year, month, day, hour, minute)
            tok = ChatToken(idx, time, user, contents)
            que.put(tok)
            idx += 1
    return (idx, que)
