import random
import time

# Implementing binary search algorithm (one of the fundamentals of Computer Science)
# Naive search is going through each items in the list
# Proven that binary search is faster than naive search because it finds the target value in the sorted list
# Then, it narrows down to the middle list to find one possible location through the sorted array
# Binary search: O(log(n)), naive search: O(n)
def naive_search(k, target):
    for n in range(len(k)):
        if k[n] == target:
            return n
    return -1


def binary_search(k, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(k) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if k[midpoint] == target:
        return midpoint
    elif target < k[midpoint]:
        return binary_search(k, target, low, midpoint-1)
    else:
        # target > k[midpoint]
        return binary_search(k, target, midpoint+1, high)

if __name__ == '__main__':
    k = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(k, target))
    print(binary_search(k, target))

    length = 10000
    # build a sorted list of length 10000
    sort_list = set()
    while len(sort_list) < length:
        sort_list.add(random.randint(-3*length, 3*length))
        # Algorithm chooses a random number and add to the list
    sort_list = sorted(list(sort_list))

    start = time.time()
    for target in sort_list:
        naive_search(sort_list, target)
    end = time.time()
    print('Naive search time:', (end - start)/length, 'seconds')

    start = time.time()
    for target in sort_list:
        binary_search(sort_list, target)
    end = time.time()
    print('Binary search time:', (end - start)/length, 'seconds')