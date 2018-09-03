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
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" % (item, count*100./n)
    print


def factorial(n): return 1 if n<=1 else n*factorial(n-1)

def shuffle(deck):
    random.shuffle(deck)

def shuffle1(deck):
    N = len(deck)
    swapped = [False]*N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)
        

def swap(deck, i, j):
    # print 'swap ', i, j
    deck[i], deck[j] = deck[j], deck[i]

def shuffle2(deck):
    N = len(deck)
    swapped = [False]*N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)


def shuffle3(deck):
    N = len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))


def test_shufflers(shufflers=[shuffle, shuffle1, shuffle2, shuffle3], decks=['abc', 'ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)


test_shufflers()

"""
function 分为两类, 一类是不修改 input, 但是返回基于 input 的新的 output; 
另一类是直接修改input, 会修改 input的状态.
前一类方法可以被称作是 pure function. 是 computing type. 更容易测试.
后一类可以被称作subroutines. 是 doing type. 
"""
