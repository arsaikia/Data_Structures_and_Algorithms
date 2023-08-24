class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Build the adjMap
        adjMap = {course: [] for course in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)

        # Do PreOrder DFS on each node
        courseSequence, visiting, visited = [], set(), set()

        for course in range(numCourses):
            if not self.canFinishCourse(course, adjMap, courseSequence, visiting, visited):
                return []

        return courseSequence

    def canFinishCourse(self, course, adjMap, courseSequence, visiting, visited):
        if course in visiting:
            return False

        if course in visited:
            return True

        visiting.add(course)
        for nextCourse in adjMap[course]:
            if not self.canFinishCourse(nextCourse, adjMap, courseSequence, visiting, visited):
                return False

        visiting.remove(course)
        visited.add(course)
        courseSequence.append(course)
        return True
