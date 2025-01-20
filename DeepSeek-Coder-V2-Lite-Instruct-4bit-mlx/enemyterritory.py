def solve(N, X, Y, start, end, bases):
    # Calculate the Manhattan distance from each base to the start and end points
    def dist_to(point):
        return abs(start[0] - point[0]) + abs(start[1] - point[1])
    
    # Calculate the Manhattan distance from each base to the end point
    dist_to_end = [abs(end[0] - base[0]) + abs(end[1] - base[1]) for base in bases]
    
    # Calculate the Manhattan distance from each base to the start point
    dist_to_start = [abs(start[0] - base[0]) + abs(start[1] - base[1]) for base in bases]
    
    # Find the minimum distance to an enemy base from either the start or end point
    min_dist = float('inf')
    for i in range(N):
        dist = max(dist_to_start[i], dist_to_end[i])
        min_dist = min(min_dist, dist)
    
    # Find the shortest route with the minimum distance to an enemy base
    min_route = float('inf')
    for i in range(N):
        if dist_to_start[i] <= min_dist and dist_to_end[i] <= min_dist:
            route = max(dist_to_start[i], dist_to_end[i])
            min_route = min(min_route, route)
    
    return f"{min_dist} {min_route}"

# Read input
N, X, Y = map(int, input().split())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
bases = [list(map(int, input().split())) for _ in range(N)]

# Solve the problem and print the result
result = solve(N, X, Y, start, end, bases)
print(result)