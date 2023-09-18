# BFS
# O(N) Time | O(N) Space
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        # build the adjMap for manager -> [ employees ]
        adjMap = collections.defaultdict(list)
        for employee, manager in enumerate(manager):
            adjMap[manager].append(employee)

        q = collections.deque([(headID, 0)])
        maxTimeReqd = 0

        while q:
            currEmployeeAsManager, timeToReachHere = q.popleft()
            maxTimeReqd = max(maxTimeReqd, timeToReachHere)

            # time Required for CurrEmployeeAsManager to inform subordinates
            timeToInformNextEmployee = timeToReachHere + \
                informTime[currEmployeeAsManager]

            for employee in adjMap[currEmployeeAsManager]:
                q.append((employee, timeToInformNextEmployee))

        return maxTimeReqd

################################################################################
# DFS
