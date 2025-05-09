import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start, goal):
        pq = [(0, start, [])]
        visited = set()

        while pq:
            cost, node, path = heapq.heappop(pq)
            if node in visited:
                continue

            path = path + [node]
            visited.add(node)

            if node == goal:
                return path, cost

            for neighbor, weight in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path))

        return None, float("inf")

g = Graph()
connections = [
    ("Arad", "Zerind", 75), ("Arad", "Sibiu", 140), ("Arad", "Timisoara", 118),
    ("Zerind", "Oradea", 71), ("Oradea", "Sibiu", 151), ("Sibiu", "Fagaras", 99), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Fagaras", "Bucharest", 211), ("Rimnicu Vilcea", "Pitesti", 97), ("Pitesti", "Bucharest", 101),
    ("Timisoara", "Lugoj", 111), ("Lugoj", "Mehadia", 70), ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120), ("Craiova", "Pitesti", 138), ("Craiova", "Bucharest", 146)
]

for u, v, w in connections:
    g.add_edge(u, v, w)

dijkstra_path, dijkstra_cost = g.dijkstra("Arad", "Bucharest")
print("Dijkstra's Algorithm (Arad to Bucharest):", dijkstra_path, "with cost:", dijkstra_cost)