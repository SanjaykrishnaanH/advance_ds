"""
Khans algorithm for topological sorting is a bfs based indegree calc tracking algo.
It is used in scenarios where, to execute step there is a pre requisite.
for exmaple like: course scheduling, cpu scheduling, and pre req based questions --> TPS
Time Complexity: O(V+E), and Space Complexity: O(V)
"""

import collections

class TopologicalSort:
    def __init__(self, n):
        self.num_of_nodes = n
        self.indegree = [0 for _ in range(n)]
        self.graph = collections.defaultdict(list)
    
    def buildGraph(self, edges):
        for u, v in edges:
            self.graph[u].append(v)
            self.indegree[v] += 1
    
    def topologicalSort(self):
        queue = [i for i in range(0, self.num_of_nodes) if self.indegree[i] == 0]
        order_of_nodes = []

        while queue:
            curr_node = queue.pop(0)
            order_of_nodes.append(curr_node)
            for nxt_node in self.graph[curr_node]:
                self.indegree[nxt_node] -= 1
                if self.indegree[nxt_node] == 0:
                    queue.append(nxt_node)
        
        if len(order_of_nodes) == self.num_of_nodes:
            return order_of_nodes
        return "Cycle found in graph"

if __name__ == "__main__":
    vertices = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    tps = TopologicalSort(vertices)
    tps.buildGraph(edges)
    result_value = tps.topologicalSort()
    print(result_value)  # Output: [5, 4, 2, 3, 1, 0]