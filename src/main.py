import lexer


def main():
    # call lexer
    chat = lexer.lex("../tests/KakaoTalkChats.txt")
    for e in chat:
        print(e)
    # pass the result to tokenizer
    # evaluate the score from tokens
    # print score
if __name__ == '__main__':
    main()
