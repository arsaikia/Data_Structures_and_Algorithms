# O(n) Time | O(n) Space
def paintHouses(costs):
    if len(costs) == 0:
        return 0

    memo = {}
    return min(getMinPrices(costs, 0, 0, memo), getMinPrices(costs, 0, 1, memo), getMinPrices(costs, 0, 2, memo))



def getMinPrices(costs, houseIdx, color, memo):
    paintCost = costs[houseIdx][color]
    if houseIdx == len(costs) - 1:
        return paintCost

    if (houseIdx, color) in memo:
        return memo[(houseIdx, color)]

    if color == 0:
        memo[(houseIdx, color)] = paintCost + min(getMinPrices(costs,
                                                               houseIdx + 1, 1, memo), getMinPrices(costs, houseIdx + 1, 2, memo))
    elif color == 1:
        memo[(houseIdx, color)] = paintCost + min(getMinPrices(costs,
                                                               houseIdx + 1, 0, memo), getMinPrices(costs, houseIdx + 1, 2, memo))
    elif color == 2:
        memo[(houseIdx, color)] = paintCost + min(getMinPrices(costs,
                                                               houseIdx + 1, 0, memo), getMinPrices(costs, houseIdx + 1, 1, memo))

    return memo[(houseIdx, color)]


if __name__ == "__main__":
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    print(paintHouses(costs))
