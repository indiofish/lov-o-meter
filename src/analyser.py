from collections import namedtuple
ChatData = namedtuple('ChatData',
                      ['interval', ])


class Analyser(object):
    """with the parsed data, gather information"""
    def __init__(self):
        super(Analyser, self).__init__()

    def analyse(self, chat):
        ret = ChatData(interval=3)

        return ret
