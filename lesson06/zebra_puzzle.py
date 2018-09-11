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
                if imright(green, ivory) #6
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegion) in orderings
                if Englishman is red #2
                if Norwegion is first #10
                if nextto(Norwegion, blue) #15
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green #4
                if Ukranian is tea #5
                if milk is middle #9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow #8
                if LuckyStrike is oj #13
                if Japanese is Parliaments #14
                for (dog, snails, fox, horse, ZEBRA) in orderings 
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )

print zebra_puzzle()