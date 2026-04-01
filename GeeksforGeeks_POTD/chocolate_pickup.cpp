class Solution {
  public:
    int n, m;
    int dp[71][71][71];
    
    int solve(int i, int j1, int j2, vector<vector<int>>& grid) {
        
        // Out of bounds
        if(j1 < 0 || j1 >= m || j2 < 0 || j2 >= m)
            return -1e8;
        
        // Base case: last row
        if(i == n - 1) {
            if(j1 == j2)
                return grid[i][j1];
            else
                return grid[i][j1] + grid[i][j2];
        }
        
        // Memoization check
        if(dp[i][j1][j2] != -1)
            return dp[i][j1][j2];
        
        int maxi = -1e8;
        
        // Try all 9 combinations
        for(int d1 = -1; d1 <= 1; d1++) {
            for(int d2 = -1; d2 <= 1; d2++) {
                
                int value;
                
                // Current cell chocolates
                if(j1 == j2)
                    value = grid[i][j1];
                else
                    value = grid[i][j1] + grid[i][j2];
                
                // Add next state
                value += solve(i + 1, j1 + d1, j2 + d2, grid);
                
                maxi = max(maxi, value);
            }
        }
        
        return dp[i][j1][j2] = maxi;
    }
    
    int maxChocolate(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        
        memset(dp, -1, sizeof(dp));
        
        return solve(0, 0, m - 1, grid);
    }
};