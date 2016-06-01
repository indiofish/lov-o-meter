from collections import namedtuple
from datetime import timedelta
import json
ChatData = namedtuple('ChatData',
                      ['interval', ])
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
        return self.__interval__(chat)

    # calculate interval between chats
    def __interval__(self, chat):
        tmp_time = timedelta(seconds=0)
        for i in range(1, len(chat)):
            tmp_time += chat[i].time - chat[i-1].time
        avg_interval = tmp_time.total_seconds() / len(chat)
        ret = ChatData(interval=avg_interval)
        return ret

    def __get_words__(self):
        with open(POSITIVE_WORDS) as fp:
            self.positive = set(json.load(fp))
        with open(NEGATIVE_WORDS) as fp:
            self.negative = set(json.load(fp))
