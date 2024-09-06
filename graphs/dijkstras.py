import math
import heapq

def dijkstra(graph, src):
    dist = [math.inf] * len(graph)
    dist[src] = 0
    pq = [(0, src)]
    heapq.heapify(pq)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > dist[curr_node]:
            continue
        for nei_node, nei_dist in enumerate(graph[curr_node]):
            if nei_dist > 0 and nei_dist != math.inf:
                if nei_dist + curr_dist < dist[nei_node]:
                    dist[nei_node] = nei_dist + curr_dist
                    heapq.heappush(pq, (nei_dist + curr_dist, nei_node))
    return dist

graph = [
    [0, 1, 4, float("inf"), float("inf"), float("inf")],
    [1, 0, 4, 2, 7, float("inf")],
    [4, 4, 0, 3, 5, float("inf")],
    [float("inf"), 2, 3, 0, 4, 6],
    [float("inf"), 7, 5, 4, 0, 7],
    [float("inf"), float("inf"), float("inf"), 6, 7, 0],
]
start_vertex = 1
result = dijkstra(graph, start_vertex)
print(f"Shortest distance from vertex {start_vertex} to all other vertices is : ")
print(result)
