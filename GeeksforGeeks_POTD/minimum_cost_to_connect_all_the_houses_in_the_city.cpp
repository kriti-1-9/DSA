class DSU {
public:
    vector<int> parent, size;

    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for(int i = 0; i < n; i++) parent[i] = i;
    }

    int findUPar(int node) {
        if(node == parent[node]) return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionBySize(int u, int v) {
        int pu = findUPar(u);
        int pv = findUPar(v);

        if(pu == pv) return;

        if(size[pu] < size[pv]) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
    }
};

class Solution {
public:
    int minCost(vector<vector<int>>& houses) {
        int n = houses.size();
        vector<tuple<int,int,int>> edges;

        // Step 1: generate all edges
        for(int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                int cost = abs(houses[i][0] - houses[j][0]) +
                           abs(houses[i][1] - houses[j][1]);
                edges.push_back({cost, i, j});
            }
        }

        // Step 2: sort edges
        sort(edges.begin(), edges.end());

        // Step 3: DSU
        DSU ds(n);
        int totalCost = 0;
        int edgesUsed = 0;

        for(auto &[cost, u, v] : edges) {
            if(ds.findUPar(u) != ds.findUPar(v)) {
                ds.unionBySize(u, v);
                totalCost += cost;
                edgesUsed++;

                if(edgesUsed == n - 1) break;
            }
        }

        return totalCost;
    }
};