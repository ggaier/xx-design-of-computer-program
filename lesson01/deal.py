import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numberhands, n=5, deck = mydeck):
    "shuffle the card and deal out numberhands n-cards hands"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numberhands)]

print deal(3)