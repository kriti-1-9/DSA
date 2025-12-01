#include <iostream>
#include <vector>
#include <list>
#include <queue>
using namespace std;

class Graph {
    int V;
    list<int>* l;

public:
    Graph(int v) {
        this->V = v;
        l = new list<int>[V];
    }

    void addEdge(int u, int v) {
        l[u].push_back(v);
        l[v].push_back(u); // For undirected graph
    }

    void printAdjList() {
        for(int i=0; i<V; i++) {
            cout << i << " : ";
            for(int nbr : l[i]) {
                cout << nbr << " ";
            }
            cout << endl;
        }
    }

    void bfs() {
        queue<int> Q;
        vector<bool> visited(V, false);
        Q.push(0);
        visited[0] = true;
        while(!Q.empty()) {
            int node = Q.front();
            Q.pop();
            cout << node << " ";
            for(int nbr : l[node]) {
                if(!visited[nbr]) {
                    Q.push(nbr);
                    visited[nbr] = true;
                }
            }
        }
    }

    void dfsHelper(int u, vector<bool>& visited) {
        cout << u << " ";
        visited[u] = true;
        for(int nbr : l[u]) {
            if(!visited[nbr]) {
                dfsHelper(nbr, visited);
            }
        }
    }

    void dfs() {
        int src = 0;
        vector<bool> visited(V, false);
        dfsHelper(src, visited);
        cout << endl;

        // for(int i=0; i<V; i++) {
        //     if(!visited[i]) {
        //         dfsHelper(i, visited);
        //     }
        // }
        // cout << endl;
    }

    bool isCycleUndirDFS(int src, int parent, vector<bool>& visited) {
        visited[src] = true;
        list<int> neighbors = l[src];
        for(int nbr : neighbors) {
            if(!visited[nbr]) {
                if(isCycleUndirDFS(nbr, src, visited)) {
                    return true;
                }
            } else if(nbr != parent) {
                return true;
            }
        }
        return false;
    }

    bool isCycle() {
        vector<bool> visited(V, false);
        for(int i=0; i<V; i++) {
            if(!visited[i]) {
                if(isCycleUndirDFS(i, -1, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    bool isCycleUndirBFS(int src, vector<bool>& visited) {
        queue<pair<int, int>> Q;
        Q.push({src, -1});
        visited[src] = true;

        while(!Q.empty()) {
            int node = Q.front().first;
            int parent = Q.front().second;
            Q.pop();

            list<int> neighbors = l[node];
            for(int nbr : neighbors) {
                if(!visited[nbr]) {
                    Q.push({nbr, node});
                    visited[nbr] = true;
                } else if(nbr != parent) {
                    return true;
                }
            }
        }
        return false;
    }

    bool isCycleBFS() {
        vector<bool> visited(V, false);
        for(int i=0; i<V; i++) {
            if(!visited[i]) {
                if(isCycleUndirBFS(i, visited)) {
                    return true;
                }
            }
        }
        return false;
    }
};

int main() {
    Graph g(5);

    g.addEdge(0, 1);
    // g.addEdge(0, 2);
    g.addEdge(0, 3);
    g.addEdge(1, 2);
    g.addEdge(3, 4);

    cout << g.isCycleBFS() << endl;
    // cout << g.isCycle() << endl;

    // g.addEdge(0, 1);
    // g.addEdge(1, 2);
    // g.addEdge(1, 3);
    // g.addEdge(2, 4);

    // g.dfs();
    // g.bfs();
    // g.printAdjList();

    return 0;
}