from collections import namedtuple
from datetime import timedelta
ChatData = namedtuple('ChatData',
                      ['interval', ])


class Analyser(object):
    """with the parsed data, gather information"""
    def __init__(self):
        super(Analyser, self).__init__()

    def analyse(self, chat):
        # calculate interval between chats
        interval = timedelta(seconds=0)
        for i in range(1, len(chat)):
            interval += chat[i].time - chat[i-1].time
        print(interval)
        ret = ChatData(interval=3)

        return ret
