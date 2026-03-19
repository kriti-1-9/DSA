"""Given a matrix of size n * m. Find the maximum path sum in the matrix. The maximum path is the sum of all elements from the first row to the last row where you are allowed to move only down or diagonally to left or right. You can start from any element in the first row.

Examples: 

Input: mat[][] = 10 10  2  0 20  4
                   1  0  0 30  2  5
                   0 10  4  0  2  0
                   1  0  2 20  0  4
Output: 74
Explanation: The maximum sum path is 20-30-4-20.

Input: mat[][] = 1 2 3
                  9 8 7
                  4 5 6
Output: 17
Explanation: The maximum sum path is 3-8-6.

Approach:
The idea is to use dynamic programming to calculate the maximum path sum in a matrix. Starting from the first row, for each cell in the matrix, we update its value by adding the maximum of the possible moves from the previous row (up, left, right). This way, we propagate the maximum possible sum at each step. Finally, we find the maximum value in the last row and return it as the result."""

# Approach: Dynamic Programming
# Language: Python

def maximum_path(mat):
    n = len(mat)
    m = len(mat[0])
    
    # Initialize result with the maximum value in the first row
    res = max(mat[0])
    
    # Traverse the matrix row by row
    for i in range(1, n):
        for j in range(m):
            # Get max value from possible previous row positions
            up = mat[i - 1][j]
            left = mat[i - 1][j - 1] if j > 0 else 0
            right = mat[i - 1][j + 1] if j < m - 1 else 0
            
            # Update current cell with max path sum
            mat[i][j] += max(up, left, right)
            
            # Update result if current cell has a greater value
            res = max(res, mat[i][j])
    
    return res

# Input matrix
mat = [
    [10, 10, 2, 0, 20, 4],
    [1, 0, 0, 30, 2, 5],
    [0, 10, 4, 0, 2, 0],
    [1, 0, 2, 20, 0, 4]
]

# Output the maximum path sum
print(maximum_path(mat))