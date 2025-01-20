import sys
from itertools import permutations

def tsp(n, m, edges):
    # Create adjacency list for the graph
    adj_list = {i: [] for i in range(n)}
    for u, v, t in edges:
        adj_list[u].append((v, t))
        adj_list[v].append((u, t))
    
    # Precompute all pairs shortest paths using Floyd-Warshall
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, t in edges:
        dist[u][v] = min(dist[u][v], t)
        dist[v][u] = min(dist[v][u], t)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Function to calculate the total time for a given permutation of hotels
    def tour_time(order):
        order = [0] + list(order) + [n-1]  # Include headquarters and attraction
        total_time = 0
        for i in range(len(order) - 1):
            total_time += dist[order[i]][order[i+1]]
        return total_time
    
    # Find the shortest tour considering all permutations of hotels
    min_tour = float('inf')
    for perm in permutations(range(1, n-1)):
        tour_time_perm = tour_time(perm)
        min_tour = min(min_tour, tour_time_perm)
    
    return min_tour

# Read input from stdin
input_lines = sys.stdin.read().splitlines()
case_num = 0
index = 0
while index < len(input_lines):
    n, m = map(int, input_lines[index].split())
    edges = []
    for i in range(m):
        u, v, t = map(int, input_lines[index + 1 + i].split())
        edges.append((u, v, t))
    index += m + 1
    
    # Solve the problem for each test case and output the result
    result = tsp(n, m, edges)
    case_num += 1
    print(f"Case {case_num}: {result}")