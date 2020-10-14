
# ----------------------------------------< Contiuous Median >--------------------------------------------------------------

class ContinuousMedianHandler:
    def __init__(self):
        self.lowerHalf = []     # MAX HEAP
        self.upperHalf = []     # MIN HEAP
        self.median = None
    # O(log n) Time | O(n) Space

    def insert(self, number):
        if not len(self.lowerHalf) or number < (-1 * self.lowerHalf[0]):
            heap.heappush(self.lowerHalf, -1 * number)
        else:
            heap.heappush(self.upperHalf, number)
        self.rebalanceHeaps()
        self.calculateMedian()

    def rebalanceHeaps(self):
        if len(self.lowerHalf) - len(self.upperHalf) == 2:
            heap.heappush(self.upperHalf, -1 * heap.heappop(self.lowerHalf))
        elif len(self.upperHalf) - len(self.lowerHalf) == 2:
            heap.heappush(self.lowerHalf, -1 * heap.heappop(self.upperHalf))

    def calculateMedian(self):
        if len(self.lowerHalf) == len(self.upperHalf):
            self.median = ((self.lowerHalf[0] * -1) + self.upperHalf[0]) / 2
        elif len(self.lowerHalf) > len(self.upperHalf):
            self.median = self.lowerHalf[0] * -1
        else:
            self.median = self.upperHalf[0]

    def getMedian(self):
        return self.median


# ------------------------------------------------< MAIN >------------------------------------------------------------------
if __name__ == "__main__":
    import heapq as heap
    median = ContinuousMedianHandler()
    median.insert(1)
    median.insert(10)
    median.insert(20)
    median.insert(30)
    median.insert(40)
    median.insert(50)
    print(median.lowerHalf, median.upperHalf, median.getMedian())
