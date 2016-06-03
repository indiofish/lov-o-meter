from collections import namedtuple, Counter
from datetime import timedelta
from analysis import sentiment
ChatData = namedtuple('ChatData',
                      ['interval',
                       'avg_chats',
                       'sentiments'])


class Analyser(object):
    """with the parsed data, gather information"""
    def __init__(self):
        super(Analyser, self).__init__()
        self.senti = sentiment.Sentiment()
        # self.__get_words__()

    def analyse(self, chat):
        interval = self.__interval__(chat)
        avg_chat = self.__chat_per_day__(chat)
        senti = self.__sentiment__(chat)
        ret = ChatData(interval=interval,
                       avg_chats=avg_chat,
                       sentiments=senti)
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
        ret = [0, 0]
        for c in chat:
            p = self.senti.analyse(c.contents)
            ret[0] += p[0]
            ret[1] += p[1]
        return ret
