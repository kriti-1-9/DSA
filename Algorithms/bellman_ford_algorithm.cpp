#include <iostream>
#include <vector>
#include <list>
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

void bellman_ford(int src, vector<list<Edge>> &g, int V) {
    vector<int> dist(V, INT_MAX);
    dist[src] = 0;

    for(int i = 1; i <= V - 1; i++) {
        for(int u = 0; u < V; u++) {
            for(Edge e : g[u]) {
                int v = e.v;
                int wt = e.wt;

                if(dist[u] != INT_MAX && dist[u] + wt < dist[v]) {
                    dist[v] = dist[u] + wt;
                }
            }
        }
    }

    // Check for negative-weight cycles
    for(int u = 0; u < V; u++) {
        for(Edge e : g[u]) {
            int v = e.v;
            int wt = e.wt;

            if(dist[u] != INT_MAX && dist[u] + wt < dist[v]) {
                cout << "Graph contains negative weight cycle" << endl;
                return;
            }
        }
    }

    for(int i = 0; i < V; i++) {
        cout << "Distance from " << src << " to " << i << " is " << dist[i] << endl;
    }
}

int main() {
    int V = 5;
    vector<list<Edge>> g(V);

    g[0].push_back(Edge(1, 10));
    g[0].push_back(Edge(2, 3));
    g[1].push_back(Edge(2, 1));
    g[1].push_back(Edge(3, 2));
    g[2].push_back(Edge(1, 4));
    g[2].push_back(Edge(3, 8));
    g[2].push_back(Edge(4, 2));
    g[3].push_back(Edge(4, 7));
    g[4].push_back(Edge(3, 9));

    bellman_ford(0, g, V);

    return 0;
}