import parser


def main():
    # call parser
    chat = parser.parse("../tests/KakaoTalkChats.txt")
    for e in chat:
        print(e)
    # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
if __name__ == '__main__':
    main()
