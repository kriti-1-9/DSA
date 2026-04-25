# Approach 1

def isSafe(grid, r, c, visited):
    n = len(grid)
    m = len(grid[0])
    return 0 <= r < n and 0 <= c < m and grid[r][c] == 'L' and not visited[r][c]
def dfs(grid, r, c, visited):
    visited[r][c] = True
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if isSafe(grid, nr, nc, visited):
            dfs(grid, nr, nc, visited)
def countIslands(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L' and not visited[i][j]:
                dfs(grid, i, j, visited)
                islands += 1
    return islands

# Approach 2

def isSafe(grid, r, c, visited):
    n = len(grid)
    m = len(grid[0])
    return (0 <= r < n and 0 <= c < m and grid[r][c] == 'L' and not visited[r][c])
def bfs(grid, visited, startR, startC):
    dRow = [-1, -1, -1, 0, 0, 1, 1, 1]
    dCol = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = deque()
    q.append((startR, startC))
    visited[startR][startC] = True
    while q:
        r, c = q.popleft()
        for k in range(8):
            newR = r + dRow[k]
            newC = c + dCol[k]
            if isSafe(grid, newR, newC, visited):
                visited[newR][newC] = True
                q.append((newR, newC))
def countIslands(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    islandCount = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'L' and not visited[r][c]:
                bfs(grid, visited, r, c)
                islandCount += 1
    return islandCount