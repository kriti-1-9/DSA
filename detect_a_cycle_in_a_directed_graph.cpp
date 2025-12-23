#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
using namespace std;

class Graph {
    int V;
    list<int> *l;
public:
    Graph(int V) {
        this->V = V;
        l = new list<int>[V];
    }

    void addEdge(int u, int v) {
        l[u].push_back(v);
    }

    bool detectCycleUtil(int node, vector<bool> &visited, vector<bool> &recStack) {
        visited[node] = true;
        recStack[node] = true;

        for (int neighbor : l[node]) {
            if (!visited[neighbor]) {
                if (detectCycleUtil(neighbor, visited, recStack))
                    return true;
            } else if (recStack[neighbor]) {
                return true;
            }
        }

        recStack[node] = false;
        return false;
    }

    bool detectCycle() {
        vector<bool> visited(V, false);
        vector<bool> recStack(V, false);

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (detectCycleUtil(i, visited, recStack))
                    return true;
            }
        }
        return false;
    }
};

int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0); // This edge creates a cycle
    g.addEdge(2, 3);

    if (g.detectCycle())
        cout << "Cycle detected in the directed graph." << endl;
    else
        cout << "No cycle detected in the directed graph." << endl;

    return 0;
}