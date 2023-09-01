###########################
# DFS
###########################
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i: [] for i in range(n)}
        for src, dst in edges:
            adjMap[src].append(dst)
            adjMap[dst].append(src)

        visited = set()
        components = 0

        def dfs(node):
            size = 0
            if node in visited:
                return 0

            # For when we have a disjoing set/ node
            if adjMap[node] == []:
                return 1

            visited.add(node)

            for nei in adjMap[node]:
                size = 1 + dfs(nei)
            return size

        for i in range(n):
            if dfs(i) > 0:
                components += 1

        return components


###########################
# DSU ( Union find )
###########################
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFindByRank = DSU(n)

        for firstNode, secondNode in edges:
            unionFindByRank.unionByRank(firstNode, secondNode)

        nodeParents = {}
        for node in range(n):
            nodeParents[node] = unionFindByRank.findParent(node)

        return len(set(nodeParents.values()))


class DSU:
    def __init__(self, n):
        self.parentMap = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def findParent(self, node):
        parent = self.parentMap[node]
        grandParent = self.parentMap[parent]

        while parent != grandParent:
            self.parentMap[parent] = self.parentMap[grandParent]
            parent = self.parentMap[parent]
            grandParent = self.parentMap[parent]

        return parent

    def unionByRank(self, firstNode, secondNode):
        firstNodeParent = self.findParent(firstNode)
        secondNodeParent = self.findParent(secondNode)

        if firstNodeParent == secondNodeParent:
            return False

        if self.rank[firstNodeParent] > self.rank[secondNodeParent]:
            self.parentMap[secondNodeParent] = firstNodeParent

        elif self.rank[firstNodeParent] < self.rank[secondNodeParent]:
            self.parentMap[firstNodeParent] = secondNodeParent

        else:
            self.parentMap[firstNodeParent] = secondNodeParent
            self.rank[secondNodeParent] += 1

        return True
