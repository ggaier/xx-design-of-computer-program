import itertools

def floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    ordering = list(itertools.permutations(floors))
    for (Hooper, Kay, Liskov, Perlis, Ritchie) in ordering:
        if (Hooper is not top
            and Kay is not bottom
            and Liskov is not top
            and Liskov is not bottom
            and Perlis > Kay
            and abs(Ritchie - Liskov) >1
            and abs(Liskov - Kay) >1 ):
            return [Hooper, Kay, Liskov, Perlis, Ritchie]

print floor_puzzle()
