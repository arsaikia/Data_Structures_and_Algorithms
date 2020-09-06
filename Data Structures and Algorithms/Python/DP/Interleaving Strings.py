import numpy as np

one = "aab"
two = "axy"
three = "aaxaby"


def interleavingStrings(one, two, three):

    cache = np.array([[None for __ in range(len(one) + 1)]
                      for __ in range(len(two) + 1)])

    cache[0][0] = True

    for col in range(1, len(cache[0])):
        if one[col - 1] == three[col - 1]:
            cache[0][col] = True
        else:
            cache[0][col] = False

    for row in range(1, len(cache)):
        if two[row - 1] == three[row - 1]:
            cache[row][0] = True
        else:
            cache[row][0] = False

    for row in range(1, len(cache)):
        for col in range(1, len(cache[0])):
            print(row-1, col-1, col + row - 1, one[col - 1], two[row - 1])

            if one[col - 1] == three[col + row - 2]:
                cache[row][col] = cache[row - 1][col]
            elif two[row - 1] == three[col + row - 2]:
                cache[row][col] = cache[row][col - 1]

    cache[row][col] = False
    print(cache)


print(interleavingStrings(one, two, three))
