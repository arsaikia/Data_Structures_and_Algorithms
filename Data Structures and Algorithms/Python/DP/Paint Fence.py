# O(n) Time | O(n) Space
def paintHouse(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    elif n == 2:
        return k * k

    cache = [0 for __ in range(n + 1)]
    cache[0] = 0
    cache[1] = k
    cache[2] = k * k

    for i in range(3, n + 1):
        cache[i] = (cache[i - 1] * (k - 1)) + (cache[i - 2] * (k - 1))

    return cache[-1]


if __name__ == "__main__":
    print(paintHouse(3, 2))
