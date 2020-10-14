
# ----------------------------------------< Numbers In PI >--------------------------------------------------------------
# TOP-DOWN
# O(n^3 + m) Space | O(n + m) Space
def minSpacesForNumbersInPi(pi, numbers):
    allNums = {num: True for num in numbers}
    cache = {}
    minSpaces = getMinSpacesStartingAtIdx(pi, allNums, 0, cache)
    return minSpaces

def minSpacesForNumbersInPiBottomUp(pi, numbers):
    allNums = {num: True for num in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpacesStartingAtIdx(pi, allNums, i, cache)
    return cache[0]

# Bottom-up
# O(n^3 + m) Space | O(n + m) Space
def getMinSpacesStartingAtIdx(pi, nums, idx, cache):
    if idx == len(pi):
        return 0
    if idx in cache:
        return cache[idx]

    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx: i + 1]
        if prefix in nums:
            currSpaces = 1 + getMinSpacesStartingAtIdx(pi, nums, i + 1, cache)
            minSpaces = min(minSpaces, currSpaces)
    cache[idx] = minSpaces
    return minSpaces


if __name__ == "__main__":
    '''Numbers in Pi'''
    pi = "3141592653589793238462643383279"
    numbers = [
        "314159265358979323846",
        "26433",
        "8",
        "3279",
        "314159265",
        "35897932384626433832",
        "79"
    ]

    print(minSpacesForNumbersInPi(pi, numbers))
    print(minSpacesForNumbersInPiBottomUp(pi, numbers))