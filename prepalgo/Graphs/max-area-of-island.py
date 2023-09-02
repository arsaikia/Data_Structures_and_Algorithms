# Recursive DFS
# O(M x N) Time || O(M x N) Space
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = [[0 for i in row] for row in grid]
        islandSize = 0

        # Iterate over each cell in grid and do dfs
        for row in range(ROW):
            for col in range(COL):
                if visited[row][col]:
                    continue
                # Get islandSize from current cell
                islandSize = max(islandSize, self.getIslandSize(
                    row, col, ROW, COL, grid, visited))

        return islandSize

    def getIslandSize(self, row, col, ROW, COL, grid, visited):
        if (row not in range(ROW) or col not in range(COL) or grid[row][col] == 0):
            return 0

        # mark visited by updating input grid
        grid[row][col] = 0

        islandSize = 1
        for r, c in self.getNeighbors(row, col, grid, ROW, COL, visited):
            islandSize += self.getIslandSize(r, c, ROW, COL, grid, visited)
        return islandSize

    def getNeighbors(self, row, col, grid, ROW, COL, visited):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        neighbors = []

        for dr, dc in directions:
            neighbors.append([row + dr, col + dc])
        return neighbors
