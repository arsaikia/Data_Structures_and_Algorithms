# BFS
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

from collections import deque


def shortestPath(grid):
    visited = [[False for __ in row] for row in grid]
    ROW, COL, pathLength = len(grid), len(grid[0]), 0

    q = deque([[0, 0]])
    visited[0][0] = True

    while q:
        print(q)
        levelSize = len(q)
        for __ in range(levelSize):
            row, col = q.popleft()

            if row == ROW - 1 and col == COL - 1:
                return pathLength

            for r, c in getNeighbors(row, col):
                if (r not in range(ROW) or c not in range(COL) or visited[r][c]):
                    continue
                visited[r][c] = True
                if grid[r][c] == 1:
                    continue
                q.append([r, c])
        pathLength += 1

    # if no path exists, return -1
    return -1


def getNeighbors(row, col):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    neighbors = []

    for dr, dc in directions:
        neighbors.append([row + dr, col + dc])

    return neighbors


# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(shortestPath(grid))
