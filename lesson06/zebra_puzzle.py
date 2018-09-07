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