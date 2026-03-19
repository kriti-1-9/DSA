#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
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

    void dfs(int curr, vector<bool> &visited, stack<int> &s) {
        visited[curr] = true;

        for (int neighbor : l[curr]) {
            if (!visited[neighbor]) {
                dfs(neighbor, visited, s);
            }
        }

        s.push(curr);
    }

    void topologicalSort() {
        vector<bool> visited(V, false);
        stack<int> s;

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, visited, s);
            }
        }
 
        while (!s.empty()) { // s.size > 0;
            cout << s.top() << " ";
            s.pop();
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

    // Topological Sorting logic would go here

    return 0;
}