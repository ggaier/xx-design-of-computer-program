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
                for (red, green, ivory, yellow, blue) in orderings 
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegion) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings 
                for (coffee, tea, milk, oj, WATER) in orderings
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Englishman is red
                if coffee is green
                if Ukranian is tea
                if imright(green, ivory)
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if Norwegion is first
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                if LuckyStrike is oj
                if Japanese is Parliaments
                if nextto(Norwegion, blue)
                )
