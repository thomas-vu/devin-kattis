def read_ints():
    return list(map(int, input().split()))

# Read the number of intersections and streets
N, M = read_ints()
# Read the start intersection, end intersection, starting time difference, and number of intersections in Mister George's route
A, B, K, G = read_ints()
# Read the intersections Mister George will visit
George_route = read_ints()

# Create a graph to store the streets and their traversal times
graph = [[] for _ in range(N + 1)]
# Read the streets and their traversal times
for _ in range(M):
    A_i, B_i, L = read_ints()
    graph[A_i].append((B_i, L))
    graph[B_i].append((A_i, L))

# Function to calculate the least amount of time Luka needs to make his delivery
def min_delivery_time(N, M, A, B, K, G, George_route, graph):
    # Create a list to store the time each intersection is free from Luka's street blocking
    free_times = [0] * (N + 1)
    
    # Calculate the time each intersection is free from Luka's street blocking
    for i in range(1, G):
        prev_inter = George_route[i - 1]
        curr_inter = George_route[i]
        travel_time = 0
        for next_inter, time in graph[prev_inter]:
            if next_inter == curr_inter:
                travel_time = time
                break
        free_start = 0 if i == 1 else free_times[prev_inter] + travel_time
        free_end = free_start + travel_time
        free_times[curr_inter] = free_end
    
    # Use Dijkstra's algorithm to find the shortest path from A to B considering Luka's starting time
    import heapq
    dist = [float('inf')] * (N + 1)
    dist[A] = K
    pq = [(K, A)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == B:
            return d
        for v, w in graph[u]:
            if free_times[v] <= d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (d + w, v))
    
    return -1  # In case there is no path from A to B

# Calculate and print the least amount of time Luka needs to make his delivery
print(min_delivery_time(N, M, A, B, K, G, George_route, graph))