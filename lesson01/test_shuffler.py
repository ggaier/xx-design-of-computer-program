import random
from collections import defaultdict

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

def test_shufflers(shufflers = [shuffle, shuffle1], decks = ['abc', 'ab']):
    for deck in decks:
        print 
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if n<=1 else n*factorial(n-1)

def shuffle(deck):
    random.shuffle(deck)

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

