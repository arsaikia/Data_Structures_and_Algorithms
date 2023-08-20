# O(m*n) Time || O(m*n) Space
class Solution:
    def getNeighbors(self, row, col):
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        neighbors = []

        for dr, dc in directions:
            neighbors.append([row + dr, col + dc])

        return neighbors

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[False for __ in row] for row in grid]
        ROW, COL, pathSize = len(grid), len(grid[0]), 0

        q = collections.deque([[0, 0]])
        visited[0][0] = True
        pathSize += 1

        while q:
            for __ in range(len(q)):
                row, col = q.popleft()

                if grid[row][col] == 1:
                    continue

                if row == ROW - 1 and col == COL - 1:
                    return pathSize

                for r, c in self.getNeighbors(row, col):
                    if (r not in range(ROW) or c not in range(COL) or visited[r][c]):
                        continue
                    visited[r][c] = True
                    if grid[r][c] == 1:
                        continue
                    q.append([r, c])

            pathSize += 1

        return -1
