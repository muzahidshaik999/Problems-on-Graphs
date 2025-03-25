# graph_coloring.py - Graph Coloring using a Greedy Algorithm
def graph_coloring(graph):
    color_map = {}
    available_colors = ["Red", "Green", "Blue"]
    
    for node in graph:
        used_colors = {color_map[neighbor] for neighbor, _ in graph[node] if neighbor in color_map}
        for color in available_colors:
            if color not in used_colors:
                color_map[node] = color
                break
    
    return color_map

graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

print(graph_coloring(graph))