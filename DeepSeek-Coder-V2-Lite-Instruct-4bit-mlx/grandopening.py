def is_possible(n, m, enclosures):
    from collections import defaultdict
    
    # Create a graph where each enclosure is a node and there's an edge between enclosures if they share an animal
    graph = defaultdict(list)
    animal_to_enclosure = {}
    
    for i in range(n):
        _, *animals = enclosures[i]
        for animal in animals:
            if animal not in animal_to_enclosure:
                animal_to_enclosure[animal] = []
            animal_to_enclosure[animal].append(i)
            
    for animal, positions in animal_to_enclosure.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                graph[positions[i]].append(positions[j])
                graph[positions[j]].append(positions[i])
    
    # Check for cycles in the graph using DFS
    visited = [False] * n
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Cycle detected
                return True
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return "POSSIBLE"
    
    # Check if all animals are already in their proper enclosures
    for enclosure in enclosures:
        _, *animals = enclosure
        for animal in animals:
            if animal != f"animal{enclosure.index(animal)}":
                return "POSSIBLE"
    
    return "FALSE ALARM"

# Read input
n, m = map(int, input().split())
enclosures = [input().split() for _ in range(n)]

# Output the result
print(is_possible(n, m, enclosures))