# O(br) Time | O(br) Space
def apartmentHunting(blocks, reqs):
    minDistanceFromBlocks = list(
        map(lambda req: getMinDistance(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(
        blocks, minDistanceFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)


def getMinDistance(blocks, req):
    minDistance = [0 for block in blocks]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistance[i] = abs(closestReqIdx - i)

    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistance[i] = min((minDistance[i]), abs(closestReqIdx - i))
    return minDistance


def getMaxDistancesAtBlocks(blocks, minDistanceFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistanceAtBlock = list(
            map(lambda distance: distance[i], minDistanceFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistanceAtBlock)
    return maxDistancesAtBlocks


def getIdxAtMinValue(array):
    idxAtValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currValue = array[i]
        if currValue < minValue:
            minValue = currValue
            idxAtValue = i
    return idxAtValue


if __name__ == "__main__":
    blocks = [
        {"gym": False, "school": True, "store": False},
        {"gym": True, "school": False, "store": False},
        {"gym": True, "school": True, "store": False},
        {"gym": False, "school": True, "store": False},
        {"gym": False, "school": True, "store": True}
    ]
    reqs = ["gym", "school", "store"]


print(apartmentHunting(blocks, reqs))
