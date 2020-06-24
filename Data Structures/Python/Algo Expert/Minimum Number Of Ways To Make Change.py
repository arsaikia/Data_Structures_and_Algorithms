# O(n) Time || O(n) Space
def minCoinsToMakeChange(n, denoms):
    coins = [float('inf') for i in range(n+1)]
    coins[0] = 0
    for denom in denoms:
        for coin in range(1, (n+1)):
            if denom <= coin:
                coins[coin] = min(coins[coin], 1 + coins[coin-denom])
    return coins[-1]


# Driver code
n = 6
denoms = [1, 2, 4]
print(minCoinsToMakeChange(n, denoms))
