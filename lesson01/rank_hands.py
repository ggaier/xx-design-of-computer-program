# -----------
# User Instructions
#
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands.
#
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will
# tell you if you are correct.


def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def hand_rank(hand):
    ranks = card_ranks(hand)
    print ranks
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return  (6, kind(3, ranks), kind(2, ranks))# your code here
    elif flush(hand):                              # flush
        return  (5, ranks) # your code here
    elif straight(ranks):                          # straight
        return  (4, max(ranks))# your code here
    elif kind(3, ranks):                           # 3 of a kind
        return  (3, kind(3, ranks), ranks)# your code here
    elif two_pair(ranks):                          # 2 pair
        return  (2, two_pair(ranks), ranks)# your code here
    elif kind(2, ranks):                           # kind
        return  (1, kind(2, ranks), ranks)# your code here
    else:                                          # high card
        return  (0, ranks)# your code here


def card_ranks(hand):
    """return a list of sorted tuples"""
    ranks = ['--23456789TJQKA'.index(rank) for rank,suit in hand]
    ranks.sort(reverse =True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks

def digital(card):
    mapping = {'T':10, "J":11, 'Q':12, 'K':13, 'A':14}
    return int(mapping.get(card[0], card[0]))

def straight(ranks):
    straight = range(ranks[-1], ranks[0]+1)
    return len(set(straight)- set(ranks))==0

def flush(hand):
    suit_set = set([s for r,s in hand])
    return len(suit_set) == 1

def kind(repeat, ranks):
    for rank in ranks:
        if ranks.count(rank) == repeat: return rank
    return None

def two_pair(ranks):
    two_pairs = set()
    for card in ranks:
        if ranks.count(card) == 2:
            two_pairs.add(card)
    if len(two_pairs) == 2:
        return tuple(two_pairs)
    else:
        return None

#To be a good programmer, you must be a good tester
def test():
    """Test case for poker function in program"""
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
    assert straight(card_ranks(al)) == True
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    print two_pair([10, 10, 5, 5, 2])
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)

    # add hand_rank assert statements
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    return "Test passed"

print test()
print card_ranks(['AC', '3D', '4S', 'KH'])  # should output [14, 13, 4, 3]
