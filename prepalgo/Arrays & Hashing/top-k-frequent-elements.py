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
