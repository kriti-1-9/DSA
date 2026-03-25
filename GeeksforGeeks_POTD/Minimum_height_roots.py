from collections import deque

class Solution:
    def findMinHeightTrees(self, V, edges):
        if V == 1:
            return [0]
        
        graph = [[] for _ in range(V)]
        degree = [0] * V
        
        # build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # initial leaves
        q = deque()
        for i in range(V):
            if degree[i] == 1:
                q.append(i)
        
        remaining = V
        
        # trim leaves
        while remaining > 2:
            size = len(q)
            remaining -= size
            
            for _ in range(size):
                node = q.popleft()
                
                for nei in graph[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        
        return list(q)