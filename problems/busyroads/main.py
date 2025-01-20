import sys
from collections import defaultdict, deque

# Read input
N, M, C = map(int, sys.stdin.readline().split())
roads = defaultdict(list)
for _ in range(M):
    A, B, T, L, R = map(int, sys.stdin.readline().split())
    roads[A].append((B, T, L, R))
    roads[B].append((A, T, L, R))

# BFS with time tracking
queue = deque([(1, 0)])  # (city, current_time)
visited = set()
min_time = float('inf')

while queue:
    city, current_time = queue.popleft()
    
    # If we reached the city N, update min_time if it's smaller
    if city == N:
        min_time = min(min_time, current_time)
        continue
    
    # Visit all roads from this city
    for next_city, travel_time, leave_time, enter_time in roads[city]:
        # Check if the road is open at current_time
        if leave_time <= current_time % C < enter_time:
            # If the next city is not visited, add it to the queue
            if (next_city, current_time + travel_time) not in visited:
                queue.append((next_city, current_time + travel_time))
                visited.add((next_city, current_time + travel_time))

# Output the minimum time to get from city 1 to city N
print(min_time)