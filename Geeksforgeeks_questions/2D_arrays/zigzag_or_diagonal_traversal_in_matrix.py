# line by line traversal

def diagonalOrder(mat):
    res = []
    n = len(mat)
    m = len(mat[0])
    for line in range(1, n + m):
        startCol = max(0, line - n)
        count = min(line, (m - startCol), n)
        for j in range(count):
            row = min(n, line) - j - 1
            col = startCol + j
            res.append(mat[row][col])
    return res

# using starting point traversal

def diagonalOrder(mat):
    res = []
    n = len(mat)
    m = len(mat[0])
    for row in range(n):
        i = row
        j = 0
        while i >= 0 and j < m:
            res.append(mat[i][j])
            i -= 1
            j += 1
        for col in range(1, m):
            i = n - 1
            j = col
            while i >= 0 and j < m:
                res.append(mat[i][j])
                i -= 1
                j += 1
    return res