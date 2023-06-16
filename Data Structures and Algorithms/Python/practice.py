# DETECT A CYCLE IN UNDIRECTED UNWEIGHTED GRAPH
# O(V + e) Time || O(V) Space

edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    []
]


def cycleInGraph(edges):
    visited = [False for __ in edges]  # [0, 0, 0, 0, 0, 0]
    inStack = [False for __ in edges]  # [0, 0, 0, 0, 0, 0]

    for node, __ in enumerate(edges):
        containsCycle = isNodeInCycle(node, edges, visited, inStack)
        if containsCycle:
            return True
    return False

# This does a DFS


def isNodeInCycle(node, edges, visited, inStack):
    visited[node] = True
    inStack[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(neighbor, edges, visited, inStack)
            if containsCycle:
                return True
        elif inStack[neighbor]:
            return True
    inStack[node] = False
    return False


print(cycleInGraph(edges))
