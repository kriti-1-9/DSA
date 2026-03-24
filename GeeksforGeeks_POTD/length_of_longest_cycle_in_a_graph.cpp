class Solution {
  public:
    int longestCycle(int V, vector<vector<int>>& edges) {
        vector<int> next(V, -1);
        
        for (auto &e : edges) {
            next[e[0]] = e[1];
        }

        vector<bool> visited(V, false);
        int ans = -1;

        for (int i = 0; i < V; i++) {
            if (visited[i]) continue;

            unordered_map<int, int> time; // node -> step
            int node = i;
            int step = 0;

            while (node != -1 && !visited[node]) {
                visited[node] = true;
                time[node] = step++;
                
                node = next[node];

                // cycle found
                if (node != -1 && time.count(node)) {
                    ans = max(ans, step - time[node]);
                    break;
                }
            }
        }

        return ans;
    }
};