class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node]) # path compression
        return self.root[node]
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if self.root[root1] != self.root[root2]:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)
    
def has_cycle(n, edges):
    uf = UnionFind(n)
    for x, y in edges:
        if uf.connected(x, y):
            return True
        uf.union(x, y)
    return False

# Example usage:
n = 5
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),
]  # This should return True as it contains a cycle
print(has_cycle(n, edges))  # Output: True

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
]  # This should return False as it doesn't contain a cycle
print(has_cycle(n, edges))  # Output: False