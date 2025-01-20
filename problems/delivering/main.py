import sys
from collections import defaultdict, deque

def min_vehicles(N, M, C, clients, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # Calculate shortest paths from the warehouse to all other junctions
    dist = [float('inf')] * N
    dist[0] = 0
    queue = deque([0])
    
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                queue.append(v)
    
    # Create a list of client indices with their shortest driving times
    clients_with_time = [(dist[client], i) for i, client in enumerate(clients)]
    clients_with_time.sort()
    
    # Assign vehicles to clients based on their shortest driving times
    assigned_clients = [False] * C
    vehicles = 0
    
    for _, client_index in clients_with_time:
        if not assigned_clients[client_index]:
            vehicles += 1
            assigned_clients[client_index] = True
    
    return vehicles

# Read input from stdin
input_data = sys.stdin.readlines()
N, M, C = map(int, input_data[0].split())
clients = list(map(lambda x: int(x) - 1, input_data[1].split()))
edges = []
for i in range(2, M + 2):
    U, V, W = map(int, input_data[i].split())
    edges.append((U - 1, V - 1, W))

# Solve the problem and output the result
print(min_vehicles(N, M, C, clients, edges))