from collections import namedtuple, Counter
from datetime import timedelta
import json
ChatData = namedtuple('ChatData',
                      ['interval', 'avg_chats'])
POSITIVE_WORDS = "../data/positive.json"
NEGATIVE_WORDS = "../data/negative.json"


class Analyser(object):
    """with the parsed data, gather information"""
    def __init__(self):
        super(Analyser, self).__init__()
        self.positive = None
        self.negative = None
        self.__get_words__()

    def analyse(self, chat):
        interval = self.__interval__(chat)
        avg_chat = self.__chat_per_day__(chat)
        self.__sentiment__(chat)
        ret = ChatData(interval=interval,
                       avg_chats=avg_chat)
        return ret

    # calculate interval between chats
    def __interval__(self, chat):
        tmp_time = timedelta(seconds=0)
        for i in range(1, len(chat)):
            tmp_time += chat[i].time - chat[i-1].time
        avg_interval = tmp_time.total_seconds() // len(chat)
        return avg_interval

    # TODO: should we use n of chats, or length?
    def __chat_per_day__(self, chat):
        cnt = Counter()
        for c in chat:
            cnt[c.time.date()] += 1
        return sum(cnt.values()) // len(cnt)

    def __sentiment__(self, chat):
        for c in chat:
            print(c.contents)

    def __get_words__(self):
        with open(POSITIVE_WORDS) as fp:
            self.positive = set(json.load(fp))
        with open(NEGATIVE_WORDS) as fp:
            self.negative = set(json.load(fp))
