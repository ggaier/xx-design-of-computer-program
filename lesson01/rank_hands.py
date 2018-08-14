def poker(hands):
    return max(hands, key=hand_rank)

def hand_rank(hand):
    return None


#To be a good programmer, you must be a good tester
def test():
    """Test case for poker function in program"""
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    return "Test passed"

print test()

