import random
from collections import defaultdict
from math import factorial


def test_shuffler(shuffler, deck = 'abcd', n=1000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)]+=1
    e = n*1./factorial(len(deck))
    ok = all((0.9<= counts[item]/e <= 1.1)
        for item in counts)
    name = shuffler.__name__
    print '%s(%s)%s' % (name, deck, ('ok' if ok else '***BAD***'))


def shuffle1(deck):
    N = len(deck)
    swapped = [False]*N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swapp(deck, i, j)
        

def swapp(deck, i, j):
    print 'swap ', i, j
    deck[i], deck[j] = deck[j], deck[i]
