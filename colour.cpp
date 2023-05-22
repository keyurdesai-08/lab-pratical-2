#include <iostream>
#include <list>
#include <vector>

class Graph {
    int V;
    std::list<int> *adj;

public:
    Graph(int V) {
        this->V = V;
        adj = new std::list<int>[V];
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    bool isSafe(int v, std::vector<int>& color, int c) {
        for (auto it = adj[v].begin(); it != adj[v].end(); ++it) {
            if (color[*it] == c)
                return false;
        }
        return true;
    }

    bool graphColoringUtil(int m, std::vector<int>& color, int v) {
        if (v == V)
            return true;

        for (int c = 1; c <= m; c++) {
            if (isSafe(v, color, c)) {
                color[v] = c;
                if (graphColoringUtil(m, color, v + 1))
                    return true;
                color[v] = 0;
            }
        }

        return false;
    }

    bool graphColoring(int m) {
        std::vector<int> color(V, 0);
        if (graphColoringUtil(m, color, 0)) {
            std::cout << "Graph can be colored with " << m << " colors.\n";
            std::cout << "Coloring Scheme:\n";
            for (int i = 0; i < V; i++)
                std::cout << "Vertex " << i << " -> Color " << color[i] << "\n";
            return true;
        }
        std::cout << "Graph cannot be colored with " << m << " colors.\n";
        return false;
    }
};

int main() {
    int V, E, m;

    std::cout << "Enter the number of vertices in the graph: ";
    std::cin >> V;
    std::cout << "Enter the number of edges in the graph: ";
    std::cin >> E;

    Graph graph(V);

    std::cout << "Enter the edges (format: source destination):\n";
    for (int i = 0; i < E; i++) {
        int u, v;
        std::cin >> u >> v;
        graph.addEdge(u, v);
    }

    std::cout << "Enter the number of colors available: ";
    std::cin >> m;

    graph.graphColoring(m);

    return 0;
}
