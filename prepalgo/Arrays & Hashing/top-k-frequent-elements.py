class Solution:
    # O(N) Time | O(N) Space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = collections.Counter(nums)
        result = []

        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in numsCounter.items():
            buckets[count].append(num)

        for idx in reversed(range(len(buckets))):
            bucket = buckets[idx]
            for num in bucket:
                if k > 0:
                    result.append(num)
                    k -= 1

        return result

################################################################
import heapq
# O(3 x N) + O(k x log N) = O(N + K log N)
# O(N) Space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        charCounter = collections.Counter(nums) # O(N)
        minHeap = [(-val, key) for key, val in charCounter.items()] # O(N)
        heapq.heapify(minHeap)  # O(N)

        res = []
        # O(k x log N)
        while k:
            __, key = heapq.heappop(minHeap)
            res.append(key)
            k -= 1
        
        return res

################################################################