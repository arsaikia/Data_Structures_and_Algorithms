# O(m x n) Time | O(m x n) Space
def numOfIslands(grid):
    visited = [[False for num in row] for row in grid]
    islands = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if visited[row][col]:
                continue
            traverseNode(row, col, grid, visited, islands)
    return islands


def traverseNode(row, col, matrix, visited, islands):
    islandSize = 0
    stack = [[row, col]]

    while stack:
        rowIdx, colIdx = stack.pop()

        visited[rowIdx][colIdx] = True

        if matrix[rowIdx][colIdx] == "0":
            continue

        islandSize += 1

        for row, col in getNeighbors(rowIdx, colIdx, matrix, visited):
            stack.append([row, col])
    if islandSize:
        islands.append(islandSize)


def getNeighbors(rowIdx, colIdx, matrix, visited):
    ROW, COL = len(matrix), len(matrix[0])
    neighbors = []
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for r, c in directions:
        row, col = rowIdx + r, colIdx + c
        if (row not in range(ROW) or col not in range(COL) or visited[row][col]):
            continue

        neighbors.append([row, col])
    return neighbors


grid = [
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "0", "0", "1"]
]

print(numOfIslands(grid))
