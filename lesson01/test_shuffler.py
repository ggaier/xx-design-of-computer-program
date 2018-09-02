import random
def test_shuffler(shuffler, deck = 'abcd', n=1000):
    counts
    return


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