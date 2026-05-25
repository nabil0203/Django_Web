import heapq

# ==================== DIJKSTRA'S ALGORITHM ====================
print("="*50)
print("DIJKSTRA'S ALGORITHM - Shortest Path")
print("="*50)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Adjacency list: {vertex: [(neighbor, weight), ...]}
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, weight):
        """Add weighted edge from u to v"""
        self.graph[u].append((v, weight))
        # For undirected graph, uncomment below:
        # self.graph[v].append((u, weight))

    def dijkstra(self, start):
        """
        Find shortest path from start to all vertices
        Time Complexity: O((V + E) log V) with min heap
        Space Complexity: O(V)
        """
        # Initialize distances with infinity
        distances = [float('inf')] * self.V
        distances[start] = 0

        # Track visited vertices
        visited = [False] * self.V

        # Min heap: (distance, vertex)
        min_heap = [(0, start)]

        while min_heap:
            # Get vertex with minimum distance
            current_dist, u = heapq.heappop(min_heap)

            # Skip if already visited
            if visited[u]:
                continue

            visited[u] = True

            # Update distances to neighbors
            for v, weight in self.graph[u]:
                if not visited[v]:
                    new_dist = current_dist + weight

                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(min_heap, (new_dist, v))

        return distances

    def dijkstra_with_path(self, start):
        """
        Find shortest path with actual path reconstruction
        Returns: (distances, previous_vertices)
        """
        distances = [float('inf')] * self.V
        distances[start] = 0

        previous = [-1] * self.V
        visited = [False] * self.V

        min_heap = [(0, start)]

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True

            for v, weight in self.graph[u]:
                if not visited[v]:
                    new_dist = current_dist + weight

                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        previous[v] = u
                        heapq.heappush(min_heap, (new_dist, v))

        return distances, previous

    def get_path(self, previous, start, end):
        """Reconstruct path from start to end"""
        path = []
        current = end

        while current != -1:
            path.append(current)
            if current == start:
                break
            current = previous[current]

        return path[::-1] if path[-1] == start else []


# ==================== EXAMPLE 1: Simple Graph ====================
print("\nExample 1: Simple Directed Graph")
print("-" * 50)

"""
Graph visualization:
    0 --4--> 1
    |        |
    2        1
    |        |
    v        v
    2 --3--> 3
    |
    7
    |
    v
    4
"""

g1 = Graph(5)
g1.add_edge(0, 1, 4)
g1.add_edge(0, 2, 2)
g1.add_edge(1, 3, 1)
g1.add_edge(2, 3, 3)
g1.add_edge(2, 4, 7)

start_vertex = 0
distances = g1.dijkstra(start_vertex)

print(f"Shortest distances from vertex {start_vertex}:")
for vertex, dist in enumerate(distances):
    if dist == float('inf'):
        print(f"  Vertex {vertex}: Unreachable")
    else:
        print(f"  Vertex {vertex}: {dist}")

print("\n")

# ==================== EXAMPLE 2: With Path Reconstruction ====================
print("Example 2: Finding Actual Paths")
print("-" * 50)

"""
Graph visualization:
    0 --1--> 1 --3--> 3
    |        |        |
    4        2        1
    |        |        |
    v        v        v
    2 --1--> 3        4
"""

g2 = Graph(5)
g2.add_edge(0, 1, 1)
g2.add_edge(0, 2, 4)
g2.add_edge(1, 2, 2)
g2.add_edge(1, 3, 5)
g2.add_edge(2, 3, 1)
g2.add_edge(3, 4, 1)

start = 0
distances, previous = g2.dijkstra_with_path(start)

print(f"Shortest paths from vertex {start}:")
for end in range(g2.V):
    if distances[end] == float('inf'):
        print(f"  To vertex {end}: Unreachable")
    else:
        path = g2.get_path(previous, start, end)
        path_str = " -> ".join(map(str, path))
        print(f"  To vertex {end}: Distance = {distances[end]}, Path = {path_str}")

print("\n")

# ==================== EXAMPLE 3: City Network ====================
print("Example 3: City Network (Practical Application)")
print("-" * 50)

class CityGraph:
    def __init__(self):
        self.graph = {}
        self.city_to_index = {}
        self.index_to_city = {}
        self.index = 0

    def add_city(self, city):
        """Add a city to the graph"""
        if city not in self.city_to_index:
            self.city_to_index[city] = self.index
            self.index_to_city[self.index] = city
            self.graph[self.index] = []
            self.index += 1

    def add_road(self, city1, city2, distance):
        """Add a road between two cities"""
        # Add cities if they don't exist
        self.add_city(city1)
        self.add_city(city2)

        # Add edges (undirected)
        idx1 = self.city_to_index[city1]
        idx2 = self.city_to_index[city2]
        self.graph[idx1].append((idx2, distance))
        self.graph[idx2].append((idx1, distance))

    def shortest_path(self, start_city, end_city):
        """Find shortest path between two cities"""
        if start_city not in self.city_to_index or end_city not in self.city_to_index:
            return None, None

        start_idx = self.city_to_index[start_city]
        end_idx = self.city_to_index[end_city]

        # Dijkstra's algorithm
        distances = [float('inf')] * self.index
        distances[start_idx] = 0
        previous = [-1] * self.index
        visited = [False] * self.index

        min_heap = [(0, start_idx)]

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True

            if u == end_idx:
                break

            for v, weight in self.graph[u]:
                if not visited[v]:
                    new_dist = current_dist + weight
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        previous[v] = u
                        heapq.heappush(min_heap, (new_dist, v))

        # Reconstruct path
        path = []
        current = end_idx
        while current != -1:
            path.append(self.index_to_city[current])
            if current == start_idx:
                break
            current = previous[current]

        path = path[::-1] if path[-1] == start_city else []

        return distances[end_idx], path


# Create city network
city_graph = CityGraph()

# Add roads (city1, city2, distance in km)
city_graph.add_road("Dhaka", "Chittagong", 264)
city_graph.add_road("Dhaka", "Sylhet", 232)
city_graph.add_road("Dhaka", "Rajshahi", 256)
city_graph.add_road("Chittagong", "Sylhet", 328)
city_graph.add_road("Chittagong", "Cox's Bazar", 152)
city_graph.add_road("Sylhet", "Rajshahi", 412)
city_graph.add_road("Rajshahi", "Khulna", 241)
city_graph.add_road("Dhaka", "Khulna", 333)

# Find shortest path
start_city = "Dhaka"
end_city = "Cox's Bazar"

distance, path = city_graph.shortest_path(start_city, end_city)

print(f"Shortest route from {start_city} to {end_city}:")
if path:
    path_str = " -> ".join(path)
    print(f"  Route: {path_str}")
    print(f"  Total Distance: {distance} km")
else:
    print("  No route found!")

print("\n")
print("All routes from Dhaka:")
for city in ["Chittagong", "Sylhet", "Rajshahi", "Khulna", "Cox's Bazar"]:
    dist, route = city_graph.shortest_path("Dhaka", city)
    if route:
        print(f"  To {city}: {dist} km via {' -> '.join(route)}")

print("\n")
