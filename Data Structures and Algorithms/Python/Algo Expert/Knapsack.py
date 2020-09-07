import numpy as np
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10
idx = len(items) - 1
memo = {}

# Top Down


def knapsack(array, capacity, idx, memo):
    if idx == 0 or capacity == 0:
        return 0

    potential = f'{idx}-{capacity - 1}'
    if potential in memo:
        return memo[potential]

    curr = array[idx]
    value = curr[0]
    weight = curr[1]

    if capacity >= weight:
        val = max(value + knapsack(array, capacity - weight, idx - 1, memo),
                  knapsack(array, capacity, idx - 1, memo))
    else:
        val = knapsack(array, capacity, idx - 1, memo)

    memo[f'{idx}-{capacity - 1}'] = val
    return val


print("Top Down", knapsack(items, capacity, idx, memo))
print(memo)


def knapsackBottomUp(array, capacity):
    cache = [[0 for col in range(capacity + 1)]
             for row in range(len(items) + 1)]
    for row in range(1, len(cache)):
        for col in range(1, len(cache[0])):
            value = array[row - 1][0]
            weight = array[row - 1][1]

            if weight > col:
                cache[row][col] = cache[row - 1][col]
            else:
                cache[row][col] = max(cache[row - 1][col],
                                      value + cache[row - 1][col - weight])

    return cache[-1][-1]


print("Bottom Up", knapsackBottomUp(items, capacity))
