class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    # O(1) Time || O(1) Space
    def peek(self):
        return self.heap[0]

    # O(1) Time || O(1) Space
    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]
        return

    # O(logN) Time || O(1) Space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap)-1)

    # O(logN) Time || O(1) Space
    def remove(self):
        self.swap(self.heap, 0, len(self.heap)-1)
        toRemove = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap)-1)
        return toRemove

    # O(logN) Time || O(1) Space
    def siftUp(self, heap, currentIdx):
        parentIdx = (currentIdx-1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(heap, currentIdx, parentIdx)
            currentIdx = parentIdx
            parentIdx = (currentIdx-1) // 2

    # O(logN) Time || O(1) Space
    def siftDown(self, heap, currentIdx, endIdx):
        childOneIdx = (currentIdx*2) + 1
        while childOneIdx < endIdx:
            childTwoIdx = (currentIdx*2) + \
                2 if (currentIdx*2) + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[currentIdx] > heap[idxToSwap]:
                self.swap(heap, currentIdx, idxToSwap)
                currentIdx = idxToSwap
                childOneIdx = (currentIdx*2)+1
            else:
                return

    # O(N) Time || O(1) Space

    def buildHeap(self, array):
        firstParentIdx = len(array)-2 // 2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(array, currentIdx, len(array)-1)
        return array


# if __name__ == "__main__":
#     minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
#     print(minHeap.peek())
