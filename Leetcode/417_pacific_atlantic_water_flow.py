class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    not visited[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Start DFS from Pacific Ocean borders
        for c in range(n):
            dfs(0, c, pacific)       # Top row
            dfs(m-1, c, atlantic)    # Bottom row
        for r in range(m):
            dfs(r, 0, pacific)       # Left column
            dfs(r, n-1, atlantic)    # Right column

        # Collect cells reachable by both oceans
        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result

        