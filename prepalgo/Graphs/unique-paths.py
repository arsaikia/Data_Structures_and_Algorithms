# O(4^(m x n)) Time | O(m x n) Space
def getPaths(grid):
    ROW = len(grid)
    COL = len(grid[0])
    visited = [[False for val in row] for row in grid]
    return dfs(0, 0, grid, visited, ROW, COL)


def dfs(row, col, matrix, visited, ROW, COL):

    if (row not in range(ROW) or
            col not in range(COL) or
            visited[row][col] or
            matrix[row][col] == 1
        ):
        return 0

    if row == (ROW - 1) and col == (COL - 1):
        return 1

    visited[row][col] = True
    count = 0
    for r, c in getNeighbors(row, col):
        count += dfs(r, c, matrix, visited, ROW, COL)
    visited[row][col] = False
    return count


def getNeighbors(row, col):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    neighbors = []

    for dr, dc in directions:
        neighbors.append([row + dr, col + dc])

    return neighbors


grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(getPaths(grid))
