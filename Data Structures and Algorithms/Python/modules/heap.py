class Heap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap) - 1)

    def remove(self):
        self.swap(self.heap, 0, len(self.heap) - 1)
        toRemove = self.heap.pop()
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        return toRemove

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]

    def siftUp(self, heap, currentIdx):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(self.heap, parentIdx, currentIdx)
            parentIdx = currentIdx
            currentIdx = (parentIdx - 1) // 2

    def siftDown(self, heap, currentIdx, endIdx):
        childOneIdx = (2 * currentIdx) + 1
        while childOneIdx < endIdx:
            childTwoIdx = (childOneIdx + 1) if (childOneIdx +
                                                1) < endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[currentIdx] > heap[idxToSwap]:
                self.swap(heap, currentIdx, idxToSwap)
                currentIdx = idxToSwap
                childOneIdx = (2 * currentIdx) + 1
            else:
                return

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(array, currentIdx, len(array) - 1)
        return array


if __name__ == "__main__":
    array = [1, -12, 8, 10, 7, 6, 2, 4]
    heap = Heap(array)
    print(heap.heap)