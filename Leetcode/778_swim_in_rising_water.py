class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]  # (time/elevation, row, col)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited[0][0] = True
        max_time = 0
        
        while min_heap:
            elevation, r, c = heapq.heappop(min_heap)
            max_time = max(max_time, elevation)
            
            # If we've reached bottom-right, return
            if r == n - 1 and c == n - 1:
                return max_time
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
        
        return -1  # Should never happen