import random


def random_list(n, u=10, l=0):
    return [random.randint(l, u-1) for i in range(n)]

def is_subset(a, b):
    '''
    return true if a is a subset of b and otherwise false
    note: this returns true if a == b (up to reordering)
    '''
    return not (False in [i in b for i in a])

def max_duplicates(a):
    '''
    returns the number of the most frequent elements
    For example: [1,2,1,7,7,7] would return 3 since
    the most frequent element, 7, appears thrice.
    '''

    return max([a.count(i) for i in a])
