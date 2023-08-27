import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortestPaths = {}

        # Build the AdjMap
        adjMap = {node: [] for node in range(1, n + 1)}
        for src, dst, timeReqd in times:
            # add as a tuple of dest, time
            adjMap[src].append((timeReqd, dst))

        # Build minHeap
        minHeap = []
        heapq.heappush(minHeap, [0, k])

        while minHeap:
            distanceToCurr, currNode = heapq.heappop(minHeap)
            if currNode in shortestPaths:
                continue
            shortestPaths[currNode] = distanceToCurr
            for distanceToNeighbor, neighborNode in adjMap[currNode]:
                heapq.heappush(
                    minHeap, [distanceToCurr + distanceToNeighbor, neighborNode])

        return max(shortestPaths.values()) if len(shortestPaths) == n else -1
