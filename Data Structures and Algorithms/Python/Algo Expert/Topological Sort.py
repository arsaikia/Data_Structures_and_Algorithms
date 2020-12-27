'''

TOPOLOGICAL SORT:
    We are given a graph ( jobs and dependencies ) and we need to find out the order in which the jobs can be completed.
'''


# O(v + e) Time | O(v + e) Space
def topologicalSort(jobs, deps):
    graph = createGraph(jobs, deps)
    return getOrderedJobs(graph)


def getOrderedJobs(graph):
    orderedNodes = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = DFS(node, orderedNodes)
        if containsCycle:
            return []
    return orderedNodes


def DFS(node, ordered):
    if node.visited:
        return False
    if node.visiting:
        return True
    for prereq in node.prereqs:
        containsCycle = DFS(prereq, ordered)
        if containsCycle:
            return True
    node.visited, node.visiting = True, False
    ordered.append(node.job)


def createGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addJobs(job)

    def addJobs(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def addPrereq(self, job, prereq):
        jobNode = self.graph[job]
        prereqNode = self.graph[prereq]
        jobNode.prereqs.append(prereqNode)


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visiting = False
        self.visited = False


if __name__ == "__main__":
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    print(topologicalSort(jobs, deps))
