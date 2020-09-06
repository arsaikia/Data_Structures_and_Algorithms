# O(nd) Time || O(n) Space
def numOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
    return ways[-1]


n = 10
denoms = [1, 5, 10, 15]
print(numOfWaysToMakeChange(n, denoms))
