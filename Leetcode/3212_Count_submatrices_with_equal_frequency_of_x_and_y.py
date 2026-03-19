class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        # prefix sum (X=+1, Y=-1)
        pref = [[0]*n for _ in range(m)]
        
        # prefix count of X
        countX = [[0]*n for _ in range(m)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                pref[i][j] = val
                countX[i][j] = 1 if grid[i][j] == 'X' else 0
                
                if i > 0:
                    pref[i][j] += pref[i-1][j]
                    countX[i][j] += countX[i-1][j]
                
                if j > 0:
                    pref[i][j] += pref[i][j-1]
                    countX[i][j] += countX[i][j-1]
                
                if i > 0 and j > 0:
                    pref[i][j] -= pref[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
                
                # check conditions
                if pref[i][j] == 0 and countX[i][j] > 0:
                    ans += 1
        
        return ans