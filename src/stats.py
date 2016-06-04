# with the given statistics of chat,
# read from json file to get precomputed
# mean and variance to calculate stuff
import math
import json
STATS = "../data/stats.json"

with open(STATS) as fp:
    statistics = json.load(fp)


def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2 * math.pi * var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


def get_stats(data):
    print(data)
    interval = data.interval
    avg_chats = data.avg_chats
    pos, neg = data.sentiments
    qa_ratio = data.qa_ratio

    interval_rank = normpdf(interval, *statistics["interval"])
    avg_chats_rank = normpdf(avg_chats, *statistics["avg_chats"])
    pos_rank = normpdf(pos, *statistics["senti_pos"])
    # neg_rank is lower the better
    neg_rank = 1 - normpdf(neg, *statistics["senti_neg"])
    qa_ratio_rank = normpdf(qa_ratio, *statistics["qa_ratio"])

    ret = (interval_rank,
           avg_chats_rank,
           pos_rank,
           neg_rank,
           qa_ratio_rank)

    # dummy value
    return ret
