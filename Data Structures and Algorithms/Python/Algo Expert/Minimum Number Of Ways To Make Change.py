# O(nd) Time || O(n) Space
def minCoinsToMakeChange(n, denoms):
    coins = [float('inf') for i in range(n+1)]
    coins[0] = 0
    for denom in denoms:
        for coin in range(1, (n+1)):
            if denom <= coin:
                coins[coin] = min(coins[coin], 1 + coins[coin-denom])
    return coins[-1] if coins[-1] != float('inf') else -1


# Driver code
n = 7
denoms = [1, 5, 10]
print(minCoinsToMakeChange(n, denoms))
