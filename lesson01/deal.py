import random
from rank_hands import hand_rank 

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
hand_names = ['Straight Flush', '4 Kind', 'Full House', 'Flush',
    'Straght', '3 Kind', '2 Pair', 'Pair', 'High Card']

def deal(numberhands, n=5, deck = mydeck):
    "shuffle the card and deal out numberhands n-cards hands"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numberhands)]

print deal(3)

def hand_percentages(n = 700*1000):
    """Sample n random hands and print a table of percentages for each type
    for each type of hand
    """
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking]+=1
    for i in reversed(range(9)):
        print "%14s: %6.3f" % (hand_names[-i-1], 100.0*counts[i]/n)

print hand_percentages(70000)