from collections import defaultdict

def topological_sort_dfs(vertices, edges):
    # Initialize the adjacency list
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
    
    visited = set()
    stack = []
    
    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)
    
    for v in range(vertices):
        if v not in visited:
            dfs(v)
    
    # Return the elements in reverse order
    return stack[::-1]

# Example usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print("Topological Sort using DFS:")
print(topological_sort_dfs(vertices, edges))
