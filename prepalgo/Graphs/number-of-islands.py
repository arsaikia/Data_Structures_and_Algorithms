# O(m x n) Time | O(m x n) Space
def numOfIslands(grid):
    visited = [[False for num in row] for row in grid]
    islands = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if visited[row][col]:
                continue
            size = traverseNode(row, col, grid, visited)
            if size:
                islands.append(size)
    return islands


def traverseNode(row, col, matrix, visited):

    if (row not in range(len(matrix)) or col not in range(len(matrix[0])) or visited[row][col]):
        return 0

    visited[row][col] = True

    if matrix[row][col] == "0":
        return 0
    return 1 + traverseNode(row + 1, col, matrix, visited) \
        + traverseNode(row - 1, col, matrix, visited) \
        + traverseNode(row, col + 1, matrix, visited) \
        + traverseNode(row, col - 1, matrix, visited)


grid = [
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "0", "0", "1"]
]

print(numOfIslands(grid))
