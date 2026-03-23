class Solution(object):
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] = (max_product, min_product)
        dp = [[(0, 0)] * n for _ in range(m)]
        
        dp[0][0] = (grid[0][0], grid[0][0])
        
        # first row
        for j in range(1, n):
            val = grid[0][j]
            prev_max, prev_min = dp[0][j-1]
            dp[0][j] = (prev_max * val, prev_min * val)
        
        # first column
        for i in range(1, m):
            val = grid[i][0]
            prev_max, prev_min = dp[i-1][0]
            dp[i][0] = (prev_max * val, prev_min * val)
        
        # rest of grid
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                top_max, top_min = dp[i-1][j]
                left_max, left_min = dp[i][j-1]
                
                candidates = [
                    top_max * val,
                    top_min * val,
                    left_max * val,
                    left_min * val
                ]
                
                dp[i][j] = (max(candidates), min(candidates))
        
        result = dp[m-1][n-1][0]
        
        if result < 0:
            return -1
        
        return result % MOD       