import parser
import jpype


def main():
    # call parser
    try:
        fp = open("../tests/KakaoTalkChats.txt", 'r', encoding='utf-8')
        jpype.attachThreadToJVM()
        chat = parser.parse(fp)
        print(chat)
        # pass the result to tokenizer
        # evaluate the score from tokens
        # print score
    except IOError:
        print("NO SUCH FILE")
if __name__ == '__main__':
    main()
