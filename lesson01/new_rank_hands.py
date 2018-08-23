def hand_rank(hand):
    groups = group(['--23456789TJQKA'.index(rank) for rank, suit in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) ==4
    flush = len(set(s for s,r in hand)) == 1
    return (9 if (5, ) == counts else
            8 if straight and flush else
            7 if (4, 1) else
            6 if (3, 2) else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) else
            2 if (2, 2, 1) else
            1 if (2, 1, 1, 1) else
            0), ranks


def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)

def test():
    pairs = group([7, 10, 7, 9, 7])
    print pairs
    print zip(pairs)
    print zip([7, 10, 9, 7, 7])
    print zip(*pairs)

print test()