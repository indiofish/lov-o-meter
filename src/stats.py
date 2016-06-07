# with the given statistics of chat,
# read from json file to get precomputed
# mean and variance to calculate stuff
import math
import json
import scipy.stats
STATS = "../data/stats.json"

with open(STATS) as fp:
    statistics = json.load(fp)


def normcdf(x, mean, sd):
    return scipy.stats.norm(mean, sd).cdf(x)


def get_stats(data):
    interval = data.interval
    avg_chats = data.avg_chats
    pos, neg = data.sentiments
    qa_ratio = data.qa_ratio

    interval_rank = 1 - normcdf(interval, *statistics["interval"])
    avg_chats_rank = normcdf(avg_chats, *statistics["avg_chats"])
    pos_rank = normcdf(pos, *statistics["senti_pos"])
    neg_rank = normcdf(neg, *statistics["senti_neg"])
    qa_ratio_rank = normcdf(qa_ratio, *statistics["qa_ratio"])

    ret = (interval_rank * 100,
           avg_chats_rank * 100,
           pos_rank * 100,
           neg_rank * 100,
           qa_ratio_rank * 100)
    print(ret)

    # dummy value
    return (ret[1]*3 + ret[0]*2 + ret[2]*2+ ret[4]*2+ret[3]) / 10
