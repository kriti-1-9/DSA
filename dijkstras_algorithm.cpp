#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

class Edge {
public:
    int v;
    int wt;

    Edge(int v, int wt) {
        this->v = v;
        this->wt = wt;
    }
};

void dijkstra(int src, vector<vector<Edge>> &g, int V) {
    vector<int> dist(V, INT_MAX);
    vector<bool> visited(V, false);

    dist[src] = 0;

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0, src});

    while(!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if(visited[u]) continue;
        visited[u] = true;

        for(Edge e : g[u]) {
            int v = e.v;
            int wt = e.wt;

            if(dist[u] + wt < dist[v]) {
                dist[v] = dist[u] + wt;
                pq.push({dist[v], v});
            }
        }
    }

    for(int i = 0; i < V; i++) {
        cout << "Distance from " << src << " to " << i << " is " << dist[i] << endl;
    }
}

int main() {
    int V = 6;
    vector<vector<Edge>> g(V);

    g[0].push_back(Edge(1, 5));
    g[0].push_back(Edge(2, 3));
    g[1].push_back(Edge(3, 6));
    g[1].push_back(Edge(2, 2));
    g[2].push_back(Edge(4, 4));
    g[2].push_back(Edge(5, 2));
    g[2].push_back(Edge(3, 7));
    g[3].push_back(Edge(5, 1));
    g[4].push_back(Edge(5, 2));

    dijkstra(0, g, V);

    return 0;
}