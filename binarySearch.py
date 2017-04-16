from random import randint


def binarySearch(s, target):
    """
    :type s: list
    :type target: int
    :rtype: int
    """
    print(s)
    l, r = 0, len(s) - 1
    while l < r:
        m = (l + r) // 2
        if s[m] == target:
            return m
        elif s[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1
binarySearch(sorted([randint(0, 50) for _ in range(30)]), 26)
