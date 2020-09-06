
# O(n) Time | O(1) Space
import minheap as M

def heapSort( array ):
    minHeap = M.MinHeap(array)
    for i in reversed(range(1, len(minHeap.heap))):
        minHeap.swap(minHeap.heap, 0, i)
        minHeap.siftDown(minHeap.heap, 0, i - 1)
    return minHeap.heap


if __name__ == "__main__":
    array = [1, -12, 8, 10, 7, 6, 2, 4]

    heapSort = heapSort(array)
    print(list(reversed(heapSort)))
    
    