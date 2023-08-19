from collections import deque
# O(m x n) Time | O(m x n) Space

###############################################################
# DFS
###############################################################


def numOfIslandsDFS(grid):
    visited = [[False for num in row] for row in grid]
    islands = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if visited[row][col]:
                continue
            size = traverseNodeDFS(row, col, grid, visited)
            if size:
                islands.append(size)
    return islands


def traverseNodeDFS(row, col, matrix, visited):

    if (row not in range(len(matrix)) or col not in range(len(matrix[0])) or visited[row][col]):
        return 0

    visited[row][col] = True

    if matrix[row][col] == "0":
        return 0
    return (1 + traverseNodeDFS(row + 1, col, matrix, visited)
            + traverseNodeDFS(row - 1, col, matrix, visited)
            + traverseNodeDFS(row, col + 1, matrix, visited)
            + traverseNodeDFS(row, col - 1, matrix, visited))

###############################################################
# BFS
###############################################################


def numOfIslandsBFS(grid):
    islands = []
    visited = [[False for __ in row] for row in grid]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if visited[row][col]:
                continue
            islandSize = traverseNodeBFS(grid, row, col, visited)
            if islandSize:
                islands.append(islandSize)
    return islands


def traverseNodeBFS(grid, row, col, visited):
    ROW, COL, islandSize = len(grid), len(grid[0]), 0
    nodesToTraverse = deque([[row, col]])

    while nodesToTraverse:
        row, col = nodesToTraverse.popleft()

        if (
            row not in range(ROW) or
            col not in range(COL) or
            visited[row][col]
        ):
            continue

        visited[row][col] = True

        if grid[row][col] == "0":
            continue

        islandSize += 1
        for r, c in getNeighbors(row, col):
            nodesToTraverse.append([r, c])
    return islandSize


def getNeighbors(row, col):
    neighbors = []
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for dr, dc in directions:
        neighbors.append([row + dr, col + dc])

    return neighbors


grid = [
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "0", "0", "1"]
]

print(numOfIslandsDFS(grid))
print(numOfIslandsBFS(grid))
