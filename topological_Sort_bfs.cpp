// Kahn's Algorithm for Topological Sorting using BFS

#include <iostream>
#include <vector>
#include <list>
#include <queue>
using namespace std;

class Graph {
    int V; // No. of vertices
    list<int> *l; // Pointer to an array containing adjacency lists

public:
    Graph(int v) {
        this->V = v;
        l = new list<int>[V];
    }

    void addEdge(int u, int v) {
        l[u].push_back(v); // Directed graph
    }

    void topoSort() {
        vector<int> res;

        //calc indegree
        vector<int> indegree(V, 0);
        for(int i = 0; i < V; i++) {
            for(int nbr : l[i]) {
                indegree[nbr]++;
            }
        }

        //0 indegree => 0
        queue<int> q;
        for(int i = 0; i < V; i++) {
            if(indegree[i] == 0) {
                q.push(i);
            }
        }

        //bfs
        while(!q.empty()) {
            int node = q.front();
            q.pop();
            res.push_back(node);

            for(int nbr : l[node]) {
                indegree[nbr]--;
                if(indegree[nbr] == 0) {
                    q.push(nbr);
                }
            }
        }

        // result
        for(int i : res) {
            cout << i << " ";
        }
        cout << endl;
    }
};

int main() {
    Graph g(6);

    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    g.topoSort();

    return 0;
}