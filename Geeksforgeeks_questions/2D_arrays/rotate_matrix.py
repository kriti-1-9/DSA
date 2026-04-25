# Expected approach 1

def rotate90(mat):
    n = len(mat)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[n - 1 - j][i]                # Move P4 to P1
            mat[n - 1 - j][i] = mat[n - 1 - i][n - 1 - j]  # Move P3 to P4
            mat[n - 1 - i][n - 1 - j] = mat[j][n - 1 - i]  # Move P2 to P3
            mat[j][n - 1 - i] = temp      # Move P1 to P2

# Expected approach 2

def rotate90(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for row in mat:
        row.reverse()