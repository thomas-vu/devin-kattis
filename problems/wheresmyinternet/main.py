def find_unconnected_houses(N, connections):
    # Create a graph to represent the connections
    graph = {i: set() for i in range(1, N + 1)}
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    
    # Perform a breadth-first search to find all connected houses
    visited = set()
    queue = [1]  # Start from house number 1 which is already connected
    
    while queue:
        house = queue.pop(0)
        visited.add(house)
        for neighbor in graph[house]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # Determine the houses that are not connected to the internet
    unconnected_houses = [house for house in range(1, N + 1) if house not in visited]
    
    # Output the result
    if unconnected_houses:
        for house in sorted(unconnected_houses):
            print(house)
    else:
        print("Connected")

# Read input
N, M = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(M)]

# Find and output the unconnected houses
find_unconnected_houses(N, connections)