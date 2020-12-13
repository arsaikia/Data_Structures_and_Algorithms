# O(V^2 + E) Time | O(V) Space
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float('inf') for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()

    while len(visited) != numberOfVertices:
        vertex, currentMinimumDistance = getVertexWithMinimumDistance(
            visited, minDistances)

        if currentMinimumDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinimumDistance + distanceToDestination
            currDestinationDistance = minDistances[destination]
            if newPathDistance < currDestinationDistance:
                minDistances[destination] = newPathDistance

    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))


def getVertexWithMinimumDistance(visited, distances):
    minVertex = None
    currentMinimumDistance = float('inf')

    for vertex, distance in enumerate(distances):
        if vertex in visited:
            continue
        if distance <= currentMinimumDistance:
            currentMinimumDistance = distance
            minVertex = vertex

    return minVertex, currentMinimumDistance
































































































































if __name__ == "__main__":
    start = 0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    print(dijkstrasAlgorithm(start, edges))
