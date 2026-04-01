class Solution {
  public:
    vector<int> tin, low, vis;
    vector<int> mark;
    int timer = 0;
    
    void dfs(int node, int parent, vector<vector<int>>& adj) {
        vis[node] = 1;
        tin[node] = low[node] = timer++;
        
        int child = 0;
        
        for(auto it : adj[node]) {
            if(it == parent) continue;
            
            if(!vis[it]) {
                dfs(it, node, adj);
                
                low[node] = min(low[node], low[it]);
                
                // Case 2: non-root
                if(low[it] >= tin[node] && parent != -1) {
                    mark[node] = 1;
                }
                
                child++;
            }
            else {
                // back edge
                low[node] = min(low[node], tin[it]);
            }
        }
        
        // Case 1: root node
        if(parent == -1 && child > 1) {
            mark[node] = 1;
        }
    }
    
    vector<int> articulationPoints(int V, vector<vector<int>>& edges) {
        
        vector<vector<int>> adj(V);
        
        // Build graph
        for(auto &e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        
        tin.resize(V);
        low.resize(V);
        vis.resize(V, 0);
        mark.resize(V, 0);
        
        // Handle disconnected graph
        for(int i = 0; i < V; i++) {
            if(!vis[i]) {
                dfs(i, -1, adj);
            }
        }
        
        vector<int> ans;
        for(int i = 0; i < V; i++) {
            if(mark[i]) ans.push_back(i);
        }
        
        if(ans.size() == 0) return {-1};
        
        return ans;
    }
};