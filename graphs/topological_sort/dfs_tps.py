import collections

class TopologicalSort:
    def __init__(self, vertices):
        self.graph = collections.defaultdict(list)
        self.V = vertices

    def buildGraph(self, edges):
        for u, v in edges:
            self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]


if __name__ == "__main__":
    vertices = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    tps = TopologicalSort(vertices)
    tps.buildGraph(edges)
    result = tps.topological_sort()
    print("Topological Sort:", result)
