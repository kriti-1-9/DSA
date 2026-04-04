class Solution {
  public:
    vector<int> diagView(vector<vector<int>> mat) {
    int n = mat.size();
    vector<int> result;

    for (int d = 0; d <= 2*n - 2; d++) {
        for (int i = 0; i <= d; i++) {
            int j = d - i;

            if (i < n && j < n) {
                result.push_back(mat[i][j]);
            }
        }
    }

    return result;
    }
};