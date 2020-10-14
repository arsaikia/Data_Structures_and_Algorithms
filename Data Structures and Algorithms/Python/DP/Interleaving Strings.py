'''
You have to use both strings completely
'''
import numpy as np


def interweaving(one, two, three):
    if len(one) + len(two) != len(three):
        return False
    cache = [[None for col in range(len(two) + 1)]
             for row in range(len(one) + 1)]

    return areInterwoven(one, two, three, 0, 0, cache)


def areInterwoven(one, two, three, i, j, cache):

    k = i + j

    if cache[i][j] is not None:
        return cache[i][j]

    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]

    cache[i][j] = False
    return False


if __name__ == "__main__":
    one = "aa"
    two = "b"
    three = "aba"
    print(interweaving(one, two, three))
