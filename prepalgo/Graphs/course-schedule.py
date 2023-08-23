class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build the adjacency map
        adjMap = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adjMap[course].append(prereq)

        # Do postorder-DFS on each node
        visiting = set()

        for course in range(numCourses):
            if not self.canFinishAllCourses(adjMap, course, visiting):
                return False
        return True

    def canFinishAllCourses(self, adjMap, course, visiting):
        if course in visiting:
            return False

        if adjMap[course] == []:
            return True

        visiting.add(course)
        for nextCourse in adjMap[course]:
            if not self.canFinishAllCourses(adjMap, nextCourse, visiting):
                return False

        visiting.remove(course)
        adjMap[course] = []
        return True
