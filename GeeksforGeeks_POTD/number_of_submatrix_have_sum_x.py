class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
    
    # Step 1: Build prefix sum matrix
        prefix = [[0]*(m+1) for _ in range(n+1)]
    
        for i in range(1, n+1):
            for j in range(1, m+1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )
    
        count = 0
    
    # Step 2: Enumerate all squares
        for i in range(1, n+1):
            for j in range(1, m+1):
            
                max_size = min(i, j)
            
                for k in range(1, max_size+1):
                
                    total = (
                        prefix[i][j]
                        - prefix[i-k][j]
                        - prefix[i][j-k]
                        + prefix[i-k][j-k]
                    )
                
                    if total == x:
                        count += 1
    
        return count