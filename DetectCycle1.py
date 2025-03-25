# cycle_detect.py - Detect Cycle in Graph using DFS
def is_cyclic(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

print("Cycle Detected:", is_cyclic(graph))