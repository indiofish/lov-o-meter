# text log parser
# import datetime
KAKAO = "카카오톡"


def parse(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
        header = f.readline()
        if KAKAO in header:
            # consume extra 1 line
            f.readline()
            return __kakao_parser__(f)
        else:
            raise IOError
    except IOError:
        print("No such file or not defined")


def __kakao_parser__(f):
    print(f.readlines())
