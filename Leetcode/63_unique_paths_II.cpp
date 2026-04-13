class Solution {
public:
    int f(int i, int j, vector<vector<int>> &dp, vector<vector<int>>& grid) {
        // out of bounds
        if(i < 0 || j < 0) return 0;

        // obstacle
        if(grid[i][j] == 1) return 0;

        // base case
        if(i == 0 && j == 0) return 1;

        // memoization
        if(dp[i][j] != -1) return dp[i][j];

        int up = f(i-1, j, dp, grid);
        int left = f(i, j-1, dp, grid);

        return dp[i][j] = up + left;
    }

    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();

        vector<vector<int>> dp(n, vector<int>(m, -1));

        return f(n-1, m-1, dp, obstacleGrid);
    }
};