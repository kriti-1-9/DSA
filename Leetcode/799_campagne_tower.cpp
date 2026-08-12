class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        // We use a 2D array to represent the tower. 
        // 101x101 is enough because the constraints say max 100 rows.
        double tower[101][101] = {0.0};
        
        // Put everything in the first glass
        tower[0][0] = (double)poured;
        
        for (int i = 0; i <= query_row; ++i) {
            for (int j = 0; j <= i; ++j) {
                // If the glass has more than 1 cup, it overflows
                if (tower[i][j] > 1.0) {
                    double overflow = (tower[i][j] - 1.0) / 2.0;
                    // Send half to the left-bottom glass
                    tower[i + 1][j] += overflow;
                    // Send half to the right-bottom glass
                    tower[i + 1][j + 1] += overflow;
                    
                    // Cap the current glass at 1.0 for the final answer
                    // (Though we only need the capped value for the final return)
                    tower[i][j] = 1.0;
                }
            }
        }
        
        // The result is the amount in the specific glass, 
        // but it cannot exceed 1.0 (it might be > 1 if we didn't cap it during simulation)
        return min(1.0, tower[query_row][query_glass]);
    }
};