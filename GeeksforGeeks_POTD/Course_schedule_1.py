from collections import deque, defaultdict

class Solution:
    def canFinish(self, n, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * n
        
        # build graph
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        # queue for nodes with indegree 0
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return count == n