# dfs.py - Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=" ")
    visited.add(start)
    
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

dfs(graph, "A")