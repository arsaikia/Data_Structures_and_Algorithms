class Solution:
    # Time: O(q + n^3)
    # Space:
    # we need to find a mapping of crs -> set of pre-requisites
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjMap = {crs: [] for crs in range(numCourses)}
        for pre, crs in prerequisites:
            adjMap[crs].append(pre)

        prereqMap, res = collections.defaultdict(set), []

        for crs in range(numCourses):
            self.buildPrereqMap(crs, adjMap, prereqMap)

        for u, v in queries:
            isValidQuery = u in prereqMap[v]
            res.append(isValidQuery)
        return res

    def buildPrereqMap(self, crs, adjMap, prereqMap):
        if crs not in prereqMap:
            prereqMap[crs] = set()
            for prereq in adjMap[crs]:
                # add the prereqs of prereq course
                prereqOfPrereqs = self.buildPrereqMap(
                    prereq, adjMap, prereqMap)
                prereqMap[crs] = prereqMap[crs].union(prereqOfPrereqs)

        prereqMap[crs].add(crs)
        return prereqMap[crs]
