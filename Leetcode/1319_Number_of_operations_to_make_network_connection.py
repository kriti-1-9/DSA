class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # union all connections
        for u, v in connections:
            union(u, v)
        
        # count components
        components = sum(1 for i in range(n) if parent[i] == i)
        
        return components - 1