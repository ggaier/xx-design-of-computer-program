import itertools

def k_combination(arr):
    combinations = []
    for i in range(len(arr)+1):
        combinations += itertools.combinations(arr, i)
    # print "combinations of array %s are: %s , total size: %s" % (arr, combinations, 
    # len(combinations))
    return combinations

def sum_of_k_combination(target_sum, combinations):
    results = []
    for c in combinations:
        if sum(c) == target_sum:
            results.append(c)
    print "combinations that sum equals %s are: %s" % (target_sum, results)
    return results

if __name__ == '__main__':
  sum_of_k_combination(10, k_combination([1, 3, 5, 7, 9, 6, 4, 8, 2, 10]))


