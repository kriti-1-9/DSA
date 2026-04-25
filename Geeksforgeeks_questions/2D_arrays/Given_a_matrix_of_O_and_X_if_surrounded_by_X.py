def fillUtil(grid, x, y, prevV, newV):
    m = len(grid)
    n = len(grid[0])
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if grid[x][y] != prevV:
        return
    grid[x][y] = newV
    fillUtil(grid, x+1, y, prevV, newV)
    fillUtil(grid, x-1, y, prevV, newV)
    fillUtil(grid, x, y+1, prevV, newV)
    fillUtil(grid, x, y-1, prevV, newV)
def fill(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                grid[i][j] = '-'
    for i in range(m):
        if grid[i][0] == '-':
            fillUtil(grid, i, 0, '-', 'O')
        if grid[i][n - 1] == '-':
            fillUtil(grid, i, n - 1, '-', 'O')
    for j in range(n):
        if grid[0][j] == '-':
            fillUtil(grid, 0, j, '-', 'O')
        if grid[m - 1][j] == '-':
            fillUtil(grid, m - 1, j, '-', 'O')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '-':
                grid[i][j] = 'X'