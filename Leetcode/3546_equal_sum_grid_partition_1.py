class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # 🔹 Horizontal cut
        prefix = 0
        for i in range(m - 1):  # ensure non-empty bottom part
            prefix += sum(grid[i])
            if prefix == target:
                return True
        
        # 🔹 Vertical cut
        colSum = [0] * n
        for j in range(n):
            for i in range(m):
                colSum[j] += grid[i][j]
        
        prefix = 0
        for j in range(n - 1):  # ensure non-empty right part
            prefix += colSum[j]
            if prefix == target:
                return True
        
        return False