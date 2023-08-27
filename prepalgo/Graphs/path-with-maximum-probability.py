import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = {}

        # Build the adjMap
        adjMap = {node: [] for node in range(n)}
        for idx, edge in enumerate(edges):
            src, dst = edge

            adjMap[src].append((dst, succProb[idx]))
            adjMap[dst].append((src, succProb[idx]))

        # build heap
        maxHeap = [(-1, start_node)]

        while maxHeap:
            currProb, currNode = heapq.heappop(maxHeap)
            if currNode in res:
                continue
            if end_node in res:
                break

            res[currNode] = currProb
            for nextNode, nextProb in adjMap[currNode]:
                heapq.heappush(maxHeap, (currProb * nextProb, nextNode))

        if end_node in res:
            return -1 * res[end_node]
        return 0
