import json
POSITIVE_WORDS = "../../data/positive.json"
NEGATIVE_WORDS = "../../data/negative.json"
SENTI_WORDS = "../../data/sentiment.json"
BOOST_WORDS = "../../data/boost.json"
NEG_WORDS = "../../data/neg.json"
EMOJIS = ['ㅋ', 'ㅡ', 'ㅠ', 'ㅎ', '^']


class Sentiment(object):
    def __init__(self):
        super(Sentiment, self).__init__()
        self.senti_words = None
        self.boost_words = None
        self.neg_words = None
        self.__get_words__()

    def __get_words__(self):
        with open(SENTI_WORDS) as fp:
            self.senti_words = json.load(fp)
        with open(BOOST_WORDS) as fp:
            self.boost_words = json.load(fp)
        with open(NEG_WORDS) as fp:
            self.neg_words = set(json.load(fp))

    def __parse_input__(self, words):
        """get a generator of words from list of
           word + tag tuples"""
        return (w[0] for w in words)

    def __weight_default__(self, words):
        l = []
        for w in words:
            # use the standard representation
            # of emojis (two characters)
            if w[0] in EMOJIS:
                w = w[0] * 2
            if w in self.senti_words:
                l.append((w, self.senti_words[w]))
            else:
                l.append((w, 0))
        return l

    def __weight_boost__(self, words):
        boost = 0
        for i, p in enumerate(words):
            weight = p[1]
            if boost:
                if weight > 0:
                    weight += boost
                    boost = 0
                elif weight < 0:
                    weight -= boost
                    boost = 0
            words[i] = (p[0], weight)
            if p[0] in self.boost_words:
                boost += self.boost_words[p[0]]

    def __weight__negate__(self, words):
        neg = 0
        for i, p in enumerate(words):
            weight = p[1]
            if neg:
                print(p)
                if weight > 0 and weight % 2 == 1:
                    weight = (weight + 1) * -0.5
                elif weight > 0 and weight % 2 == 0:
                    weight *= -0.5
                else:
                    weight = 0
            words[i] = (p[0], weight)
            neg = p[0] in self.neg_words

    def __reverse__(self, sentence):
        """some phrases totally change the meaning
        ex) 싫지 않아"""
        rev = 0
        for w, tag in sentence:
            if (w in self.neg_words and
                    tag in ['VXV']):
                rev = not rev
        return rev

    def __get_avg__(self, words):
        pos, neg = 0, 0
        for p in words:
            if p[1] > 0:
                pos += p[1]
            elif p[1] < 0:
                neg += p[1]
        pos /= len(words)
        neg /= len(words)

        return (pos, neg)

    def senti(self, sentence):
        words = self.__parse_input__(sentence)

        default = self.__weight_default__(words)
        self.__weight_boost__(default)
        self.__weight__negate__(default)

        avg = self.__get_avg__(default)
        if self.__reverse__(sentence):
            avg = (-avg[1], -avg[0])
        return avg


def main():
    sent = Sentiment()
    print(sent.senti([('존',''),('좋','')]))

if __name__ == '__main__':
    main()
