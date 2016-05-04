import parser


def main():
    # call parser
    fp = open("../tests/KakaoTalkChats.txt", 'r', encoding='utf-8')
    chat = parser.parse(fp)
    # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
if __name__ == '__main__':
    main()
