import heapq

def dijkstra(graph, start, target):
    pq = []  # Min-heap priority queue
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

# Graph representation
Graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

shortest_distance, path = dijkstra(Graph, "A", "F")
print(f"Shortest Path from A to F: {path} with distance {shortest_distance}")
