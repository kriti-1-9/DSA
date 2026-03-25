class Solution {
public:
    int n;
    vector<vector<int>> grid;
    unordered_map<int, int> islandSize;

    int dfs(int i, int j, int id) {
        if(i < 0 || j < 0 || i >= n || j >= n || grid[i][j] != 1)
            return 0;
        
        grid[i][j] = id;
        
        return 1 + dfs(i+1, j, id)
                 + dfs(i-1, j, id)
                 + dfs(i, j+1, id)
                 + dfs(i, j-1, id);
    }

    int largestIsland(vector<vector<int>>& g) {
        grid = g;
        n = grid.size();
        
        int id = 2; // start from 2 to distinguish from 0 and 1
        
        // 🔹 Step 1: Label islands
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    int size = dfs(i, j, id);
                    islandSize[id] = size;
                    id++;
                }
            }
        }

        int ans = 0;

        // 🔹 Step 2: Try flipping each 0
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 0) {
                    unordered_set<int> seen;
                    int currSize = 1; // flipping this 0

                    vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};

                    for(auto &d : dirs) {
                        int ni = i + d.first;
                        int nj = j + d.second;

                        if(ni >= 0 && nj >= 0 && ni < n && nj < n) {
                            int nid = grid[ni][nj];
                            if(nid > 1 && seen.find(nid) == seen.end()) {
                                currSize += islandSize[nid];
                                seen.insert(nid);
                            }
                        }
                    }

                    ans = max(ans, currSize);
                }
            }
        }

        // 🔹 Step 3: If no zero found
        if(ans == 0) return n * n;

        return ans;
    }
};