import heapq

# O( n log(k) + k ) Time | O(n + k) Space


def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIdx in range(len(arrays)):
        smallestItems.append(
            {"arrayIdx": arrayIdx, "elementIdx": 0, "num": arrays[arrayIdx][0]})

    minHeap = []
    for item in smallestItems:
        heapq.heappush(
            minHeap, (item["num"], item["arrayIdx"], item["elementIdx"]))

    while len(minHeap):
        smallestElement = heapq.heappop(minHeap)
        num, arrayIdx, elementIdx = smallestElement
        sortedList.append(num)
        if elementIdx == len(arrays[arrayIdx]) - 1:
            continue

        heapq.heappush(
            minHeap, (arrays[arrayIdx][elementIdx + 1], arrayIdx,  elementIdx + 1))

    return sortedList


if __name__ == "__main__":
    arrays = [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]
    print(mergeSortedArrays(arrays))
