import json
DATE_WORDS = "../data/date.json"
OK_WORDS = "../data/ok.json"
REFUSE_WORDS = "../data/refuse.json"
QUESTIONS = ['EFQ', 'EFO', 'EFA']

with open(DATE_WORDS) as fp:
    date_words = json.load(fp)
with open(OK_WORDS) as fp:
    ok_words = json.load(fp)
with open(REFUSE_WORDS) as fp:
    refuse_words = json.load(fp)


def is_question(sentence):
    # get last token
    tok, tag = sentence[-1]
    if '?' in tok or tag in QUESTIONS:
        return True
    else:
        return False


def reply(sentence):
    for tok, tag in sentence:
        if tok in ok_words:
            return 1
        if tok in refuse_words:
            return -1
    else:
        return 0


def score(q):
    nouns = (w[0] for w in q if w[1] == 'NNG')
    # a question's default score is 1
    ret = 1
    for w in nouns:
        if w in DATE_WORDS:
            ret += 1
    return ret
