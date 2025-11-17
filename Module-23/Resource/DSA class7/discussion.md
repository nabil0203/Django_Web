### **DSA Lecture: Graphs - Implementation and Traversal**


---

### **1. Introduction **

**What is a Graph?**

Imagine a social network like Facebook or Instagram. Each person is a **vertex** (or **node**), and when two people are friends, there's a connection between them, which we call an **edge**. A graph is simply a collection of these vertices and edges.

Graphs are used everywhere in our digital lives. They power:

*   **Social Networks:** Recommending friends and analyzing connections.
*   **Navigation Apps:** Google Maps and Waze use graphs to find the shortest route from your home to school, avoiding traffic.
*   **Search Engines:** Google uses graphs to understand how web pages are linked together to give you the most relevant search results.
*   **E-commerce Websites:** Amazon and Netflix use graphs to recommend products and movies based on what you and others with similar tastes have viewed.

**Key Terminology:**

*   **Vertex (Node):** A fundamental unit of a graph (e.g., a person in a social network).
*   **Edge:** A connection between two vertices (e.g., a friendship).
*   **Degree:** The number of edges connected to a vertex.
*   **Undirected Graph:** Edges have no direction. If A is friends with B, B is also friends with A.
*   **Directed Graph:** Edges have a direction. If A follows B on Instagram, it doesn't necessarily mean B follows A.
*   **Weighted Graph:** Edges have a weight or cost. In a navigation app, the weight of an edge between two locations could be the travel time or distance.

**Example Graph:**

Let's visualize a simple undirected graph:

*   **Vertices:** A, B, C, D
*   **Edges:** A-B, A-C, A-D, B-C

This could represent a group of friends where A is friends with B, C, and D, and B is also friends with C.

---

### **2. Graph Representations**

How do we represent a graph in a way a computer can understand? There are two main methods:

#### **2.1 Adjacency Matrix**

An adjacency matrix is a 2D array (like a grid or a spreadsheet) where we use `1` to indicate an edge exists between two vertices and `0` if it doesn't.

For our example graph (A, B, C, D), the adjacency matrix would look like this:

|       | **A** | **B** | **C** | **D** |
| :---: | :---: | :---: | :---: | :---: |
| **A** |   0   |   1   |   1   |   1   |
| **B** |   1   |   0   |   1   |   0   |
| **C** |   1   |   1   |   0   |   0   |
| **D** |   1   |   0   |   0   |   0   |

Notice that the matrix is symmetric for an undirected graph because if there's an edge from A to B, there's also one from B to A.

**Python Implementation:**
```python
vertexData = ['A', 'B', 'C', 'D']
adjacency_matrix = [
    [0, 1, 1, 1],  # A
    [1, 0, 1, 0],  # B
    [1, 1, 0, 0],  # C
    [1, 0, 0, 0]   # D
]

def print_connections(matrix, vertices):
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end=" ")
        print()
```

#### **2.2 Adjacency List**

An adjacency list is often more space-efficient for graphs with few connections. Here, each vertex has a list of its neighbors.

**Python Implementation (using a dictionary):**
```python
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['A']
}
```

**Advantages of Adjacency List:**
*   Saves space for sparse graphs (graphs with few edges).
*   Faster to find all neighbors of a vertex.

---

### **3. Graph Implementation Using Classes**

To keep our code organized and reusable, we can create a `Graph` class.

#### **Undirected Graph Class:**
```python
class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
        print("\nVertex Data:", self.vertex_data)

# Example Usage:
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.print_graph()
```

#### **Directed and Weighted Graphs:**

*   **For a directed graph**, we would only set `self.adj_matrix[u][v] = 1` and not the other way around.
*   **For a weighted graph**, instead of `1`, we would store the actual weight of the edge.

```python
def add_edge(self, u, v, weight=1, directed=False):
    self.adj_matrix[u][v] = weight
    if not directed:
        self.adj_matrix[v][u] = weight
```

---

### **4. Graph Traversal**

Graph traversal is the process of visiting all the vertices in a graph in a systematic way.

#### **4.1 Depth-First Search (DFS)**

DFS explores as far as possible along each branch before backtracking. It's like navigating a maze by always taking the same turn (e.g., always turn right) until you hit a dead end, then you backtrack and try a different path.

DFS is often implemented using recursion or a stack. It is useful for tasks like solving puzzles, detecting cycles in a graph, and topological sorting (ordering tasks with dependencies).

**DFS Example Execution:**
Consider the following directed graph:
*   **Edges:** D -> A, D -> E, A -> C, C -> F, C -> G, F -> B, B -> C

**A DFS starting from D would visit the nodes in this order:** D, A, C, F, B, G, E

**Python Implementation:**
```python
def dfs_util(self, v, visited):
    visited[v] = True
    print(self.vertex_data[v], end=' ')
    for i in range(self.size):
        if self.adj_matrix[v][i] == 1 and not visited[i]:
            self.dfs_util(i, visited)

def dfs(self, start_vertex_data):
    visited = [False] * self.size
    try:
        start_index = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_index, visited)
    except ValueError:
        print(f"Vertex {start_vertex_data} not found.")
```

#### **4.2 Breadth-First Search (BFS)**

BFS explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. It's like dropping a stone in a pond and watching the ripples spread out, level by level.

BFS is implemented using a queue. It is excellent for finding the shortest path in an unweighted graph, which is how GPS systems find the nearest locations. It's also used by search engine crawlers to index web pages.

**Python Implementation:**
```python
from collections import deque

def bfs(self, start_vertex_data):
    visited = [False] * self.size
    try:
        start_index = self.vertex_data.index(start_vertex_data)
        queue = deque([start_index])
        visited[start_index] = True

        while queue:
            current = queue.popleft()
            print(self.vertex_data[current], end=' ')
            for i in range(self.size):
                if self.adj_matrix[current][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
    except ValueError:
        print(f"Vertex {start_vertex_data} not found.")

```

#### **Notes on Traversals:**

*   **DFS:** Good for pathfinding, finding connected components, and topological sorting.
*   **BFS:** Excellent for finding the shortest path in unweighted graphs and level-order traversal.
*   Both work for directed and undirected graphs.

---

### **5. Homework**
1.  Implement the graph from the activity in Python using the `Graph` class.
2.  Write a program that uses DFS to check if there is a path between two vertices in your graph.
3.  Write a program that uses BFS to find the shortest path (in terms of the number of edges) between two vertices in your graph.
