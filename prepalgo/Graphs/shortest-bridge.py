class Solution:
    # Approach:
    #           1. Traverse to find a 1 in grid
    #           2. DFS on cell to find one island
    #           3. BFS starting with island nodes found in prev step
    #           4. If you see another land, return steps taken in BFS
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        # Traverse to find a 1 in grid
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    # DFS on cell to find one island
                    self.findIslandCellsUsingDfs(grid, row, col, visited)

                    # BFS starting with island nodes found in prev step
                    return self.searchForNextIslandUsingBfs(visited, grid)
        return -1

    def notInGrid(self, grid, r, c):
        ROWS, COLS = len(grid), len(grid[0])
        if r not in range(ROWS) or c not in range(COLS):
            return True
        return False

    def findIslandCellsUsingDfs(self, grid, row, col, visited):
        if self.notInGrid(grid, row, col) or grid[row][col] == 0 or (row, col) in visited:
            return

        visited.add((row, col))

        # Find connected 1's
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            r, c = row + dr, col + dc
            self.findIslandCellsUsingDfs(grid, r, c, visited)

    def searchForNextIslandUsingBfs(self, visited, grid):
        q = collections.deque(visited)
        bridgeSize = 0

        while q:
            for __ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    r, c = row + dr, col + dc

                    if self.notInGrid(grid, r, c) or (r, c) in visited:
                        continue

                    if grid[r][c] == 1:
                        return bridgeSize

                    q.append((r, c))
                    visited.add((r, c))

            bridgeSize += 1

        return bridgeSize
