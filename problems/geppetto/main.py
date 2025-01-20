from sys import stdin, stdout
import itertools

def count_different_pizzas(N, M, restrictions):
    # Create a graph where each ingredient is a node and edges represent the prohibition of mixing ingredients
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in restrictions:
        graph[a].append(b)
        graph[b].append(a)
    
    # Helper function to check if a pizza is valid
    def is_valid(pizza):
        for ingredient in pizza:
            for neighbor in graph[ingredient]:
                if neighbor in pizza:
                    return False
        return True
    
    # Generate all possible pizzas and count the valid ones
    total_pizzas = 0
    for r in range(1, N + 1):
        for combo in itertools.combinations(range(1, N + 1), r):
            if is_valid(combo):
                total_pizzas += 1
    
    return total_pizzas

# Read input
N, M = map(int, stdin.readline().split())
restrictions = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

# Calculate and output the result
result = count_different_pizzas(N, M, restrictions)
stdout.write(str(result) + '\n')