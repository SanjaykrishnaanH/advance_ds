import copy

def floyd_warshall(graph, len_graph):
    dp = copy.deepcopy(graph)
    for k in range(0, len_graph):
        for i in range(0, len_graph):
            for j in range(0, len_graph):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]
len_graph = len(graph)
result = floyd_warshall(graph, len_graph)
for row in result:
    print(row)
