blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True}
]

reqs = ["gym", "school", "store"]

# O(b x r) Time | O(b x r) Space
def apartmentHunting( blocks, reqs ):
    minReqDistanceFromBlocks = list( map( lambda req: getMinDistances(blocks, req) , reqs) )
    minDistancesAtBlocks = getMaxDistanceAtBlocks(blocks, minReqDistanceFromBlocks)
    return getIdxWithMinValue(minDistancesAtBlocks)


def getMinDistances(blocks, req):
    minDistances = [0 for i in range(len(blocks))]
    closestReqIdx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = abs(i - closestReqIdx)
    
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], abs(i - closestReqIdx))
        
    return minDistances

def getMaxDistanceAtBlocks(blocks, minReqDistanceFromBlocks):
    maxDistancesAtBlocks = [ 0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i] , minReqDistanceFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    
    return maxDistancesAtBlocks

    
        
def getIdxWithMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currVal = array[i]
        if currVal < minValue:
            minValue = currVal
            idxAtMinValue = i
    return idxAtMinValue
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    print(apartmentHunting(blocks, reqs))