def spirallyTraverse(mat):
    n = len(mat)
    m = len(mat[0])
    res = []
    vis = [[False] * m for _ in range(n)]
    dr = [0, 1, 0, -1]
    cr = [1, 0, -1, 0]
    r, c = 0, 0
    idx = 0
    for _ in range(n * m):
        res. append(mat[r][c])
        vis[r][c] = True
        nr, nc = r + dr[idx], c + cr[idx]
        if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:
            r, c = newR, newC
        else:
            idx = (idx + 1) % 4
            r += dr[idx]
            c += dc[idx]
    return res

def spirallyTraverse(mat):
    m, n = len(mat), len(mat[0])
    res = []
    top, bottom, left, right = 0, m-1, 0, n-1
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            res.append(mat[top][i])
        top += 1
        for i in range(top, bottom+1):
            res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(mat[i][left])
            left += 1
    return res