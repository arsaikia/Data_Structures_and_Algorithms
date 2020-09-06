
def orangesRotting(grid):
    values = {"timeElapsed": 0, "oneFound": 0}
    traversed = [[True if col == 2 else False for col in row] for row in grid]
    print(traversed)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue
            elif grid[row][col] == 1:
                values["oneFound"] += 1
            else:
                if traversed[row][col]:
                    values["timeElapsed"] -= 1
                traverseRotten(row, col, grid, values, traversed)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return -1

    return values["timeElapsed"]


def traverseRotten(row, col, grid, values, traversed):
    node = [[row, col]]
    while len(node):
        curr = node.pop()
        i = curr[0]
        j = curr[1]

        neighbors = getNeighbors(i, j, grid, values, traversed)
        node.extend(neighbors)


def getNeighbors(row, col, grid, values, traversed):
    result = []

    if row > 0 and grid[row-1][col] == 1:
        grid[row-1][col] = 2
        result.append([row-1, col])

    if row < len(grid) - 1 and grid[row + 1][col] == 1:
        grid[row + 1][col] = 2
        result.append([row+1, col])

    if col > 0 and grid[row][col - 1] == 1:
        grid[row][col - 1] = 2
        result.append([row, col-1])

    if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
        grid[row][col + 1] = 2
        result.append([row, col+1])

    if len(result):
        values["timeElapsed"] += 1
    return result


if __name__ == "__main__":
    matrix = [[1,2,1,1,2,1,1]]
    print(orangesRotting(matrix))
