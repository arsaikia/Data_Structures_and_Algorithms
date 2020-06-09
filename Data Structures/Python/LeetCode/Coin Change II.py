from typing import List
def change(amount: int, coins: List[int]) -> int:
    dp = [0 for i in range(amount+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    return dp


print(change(5, [1,2,5]))