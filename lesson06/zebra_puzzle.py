#itertools.permutaions(list) function

#python handle small integers as identical, so use `is` also same as ==

import itertools

houses = [1, 2, 3, 4, 5]

# permutations function: all possible full-length permutations are generated
ordering = list(itertools.permutations(houses))

def imright(h1, h2):
    return (h1-h2)==1

def nextto(h1, h2):
    return abs(h1-h2) ==1

print nextto(2, 3)

def zebra_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA) 
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory) #6
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegion) in c(ordering)
                if Englishman is red #2
                if Norwegion is first #10
                if nextto(Norwegion, blue) #15
                for (coffee, tea, milk, oj, WATER) in c(ordering)
                if coffee is green #4
                if Ukranian is tea #5
                if milk is middle #9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(ordering)
                if Kools is yellow #8
                if LuckyStrike is oj #13
                if Japanese is Parliaments #14
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

# print zebra_puzzle()

import time
def timedcall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    print t1-t0, result
    return (t1 - t0, result)

def averge(numbers):
    return sum(numbers)/ float(len(numbers))

def timedCalls(n, fn, *args):
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times)<n:
            times.append(timedcall(fn, *args)[0])
    return min(times), averge(times), max(times)

def instrument_fn(fn, *args):
    "Another key feature is that the local variables and execution state are automatically saved between calls."
    c.starts, c.items = 0, 0
    result = fn(*args)
    print '%s got %s with %d iters over %7d times' % (fn.__name__, result, c.starts, c.items)

def c(sequence):
    c.starts +=1
    for item in sequence:
        c.items +=1
        yield item


def ints(start, end=None):
    i = start
    while i <= end or end is None:
        yield i
        i = i+1


def all_ints():
    yield 0 
    print 0
    for i in ints(1):
        yield +i
        yield -i

instrument_fn(zebra_puzzle)
