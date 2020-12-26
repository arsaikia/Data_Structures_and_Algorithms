# # O(V^2 + E) Time | O(V) Space
# def dijkstrasAlgorithm(start, edges):
#     numberOfVertices = len(edges)

#     minDistances = [float('inf') for _ in range(numberOfVertices)]
#     minDistances[start] = 0

#     visited = set()

#     while len(visited) != numberOfVertices:
#         vertex, currentMinimumDistance = getVertexWithMinimumDistance(
#             visited, minDistances)

#         if currentMinimumDistance == float('inf'):
#             break

#         visited.add(vertex)

#         for edge in edges[vertex]:
#             destination, distanceToDestination = edge

#             if destination in visited:
#                 continue

#             newPathDistance = currentMinimumDistance + distanceToDestination
#             currDestinationDistance = minDistances[destination]
#             if newPathDistance < currDestinationDistance:
#                 minDistances[destination] = newPathDistance

#     return list(map(lambda x: -1 if x == float('inf') else x, minDistances))


# def getVertexWithMinimumDistance(visited, distances):
#     minVertex = None
#     currentMinimumDistance = float('inf')

#     for vertex, distance in enumerate(distances):
#         if vertex in visited:
#             continue
#         if distance <= currentMinimumDistance:
#             currentMinimumDistance = distance
#             minVertex = vertex

#     return minVertex, currentMinimumDistance


# if __name__ == "__main__":
#     start = 0
#     edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
#     print(dijkstrasAlgorithm(start, edges))

'''
Dijkstra Algorithm to find shortest Paths in a graph:
    It is used to find the shortest path from one source to all other nodes in a Directed Weighted Graph
    We are given :
        The source Node
        All the other nodes and their distances as an adjacency list
    
    Adjacency List:
        An adjacency list is a list of lists
        where the index of each list is the current node we are considering and 
        each inner list has the destination node as the first index and the distance to that node in the second index

    Approach:
        Make a distances list which stores the min distances to each node from source.
        We will keep a visited set and when the length of the visited set is equals to the distances we return distances.

        When length of visited < length of distances:
            Find the minimum distance that is not visited:
                if we use an array:
                    in O(n) time traverse the distances and idx -> Node and distance is distance

            For th minimum distances node, find the edge : each edge gives us the distance to that node and if the distance from the 
            adjacency list + current node distance from source ism smaller tha what we already had in the list, update

            make the current node as visited.

        return list( map( lambda( x : -1 if x == float('inf) else x ) , distances) )  

'''

from typing import List


def dijkstraAlgorithm(startNode: int, edges):
    numOfVertices = len(edges)
    distances = [float('inf') for _ in range(numOfVertices)]
    distances[startNode] = 0
    visited = set()

    while len(visited) < numOfVertices:
        node, distanceToNode = getNextSmallestNodeDistance(distances, visited)

        if distanceToNode == float('inf'):
            break

        visited.add(node)

        for destination, distanceToDestination in edges[node]:
            if destination in visited:
                continue
            newDistance = distanceToNode + distanceToDestination
            distances[destination] = min(newDistance, distances[destination])
    return list(map(lambda x: -1 if x == float('inf') else x, distances))


def getNextSmallestNodeDistance(distances, visited):
    node = None
    minDistance = float('inf')

    for nodeIdx, distanceToNode in enumerate(distances):
        if nodeIdx in visited:
            continue
        if distanceToNode <= minDistance:
            minDistance = distanceToNode
            node = nodeIdx
    return node, minDistance


if __name__ == "__main__":
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    startNode = 0

    print(dijkstraAlgorithm(startNode, edges))
