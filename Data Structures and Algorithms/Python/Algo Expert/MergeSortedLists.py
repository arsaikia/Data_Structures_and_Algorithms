
import heapq as minHeap


def mergeSortedList(arrays):
    sortedList = []
    smallestElements = []
    for arrayIdx in range(len(arrays)):
        currentElement = (arrays[arrayIdx][0], arrayIdx, 0)
        smallestElements.append(currentElement)

    minHeap.heapify(smallestElements)

    while len(smallestElements):
        smallestElement = minHeap.heappop(smallestElements)
        num, arrayIdx, elIdx = smallestElement
        sortedList.append(num)
        if elIdx == len(arrays[arrayIdx]) - 1:
            continue
        minHeap.heappush(smallestElements,
                         (arrays[arrayIdx][elIdx + 1], arrayIdx, elIdx + 1))

        # break

    print(sortedList)


if __name__ == "__main__":
    array = [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]
    mergeSortedList(array)
