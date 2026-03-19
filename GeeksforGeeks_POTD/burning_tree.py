'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        parent = {}
        target_node = None
        
        def dfs(node, par):
            nonlocal target_node
            if not node:
                return
            
            if node.data == target:
                target_node = node
            
            parent[node] = par
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        # Step 2: BFS from target
        q = deque([target_node])
        visited = set([target_node])
        time = -1
        
        while q:
            size = len(q)
            time += 1
            
            for _ in range(size):
                node = q.popleft()
                
                for nei in [node.left, node.right, parent[node]]:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        
        return time