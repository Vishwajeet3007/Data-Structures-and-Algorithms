import itertools

def calculate_distance(graph, path):
  
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Return to the starting point
    return total_distance

def travelling_salesman_problem(graph):
  
    num_vertices = len(graph)
    vertices = list(range(num_vertices))
    
    min_path = None
    min_distance = float('inf')
    
    # Generate all possible permutations of the vertices
    for perm in itertools.permutations(vertices):
        current_distance = calculate_distance(graph, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm
    
    return min_distance, min_path

# Example graph represented as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve the TSP
min_distance, min_path = travelling_salesman_problem(graph)

# Output the result
print("Minimum distance:", min_distance)
print("Optimal path:", min_path)
