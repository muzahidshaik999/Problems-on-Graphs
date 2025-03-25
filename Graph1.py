import heapq
from collections import deque

# Graph representation as adjacency list
Graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

### Problem 1: Dijkstra’s Algorithm for Shortest Path (A to F)
def dijkstra(graph, start, target):
    pq = []  # Priority queue (min-heap)
    heapq.heappush(pq, (0, start))  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {start: None}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == target:
            break  # Reached the target

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    # Reconstruct path
    path = []
    node = target
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return distances[target], path

shortest_distance, path = dijkstra(Graph, "A", "F")
print(f"Shortest Path from A to F: {path} with distance {shortest_distance}")


### Problem 2: Breadth-First Search (BFS)
def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    bfs_order = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

print("BFS Traversal:", bfs(Graph, "A"))


### Problem 3: Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_order.append(start)

    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs_order = []
dfs(Graph, "A")
print("DFS Traversal:", dfs_order)


### Problem 4: Cycle Detection (DFS)
def detect_cycle(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Cycle detected
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return "Cycle Detected"
    
    return "No Cycle Detected"

print(detect_cycle(Graph))


### Problem 5: Graph Coloring (Greedy Algorithm)
def graph_coloring(graph):
    color_assignment = {}
    colors = ['Red', 'Green', 'Blue']  # 3 available colors

    for node in graph:
        used_colors = set(color_assignment.get(neighbor) for neighbor, _ in graph[node] if neighbor in color_assignment)
        
        for color in colors:
            if color not in used_colors:
                color_assignment[node] = color
                break

    return color_assignment

print("Node Colors:", graph_coloring(Graph))
