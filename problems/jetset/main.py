def find_missing_meridian(n, waypoints):
    visited = [False] * n
    missing_meridian = None
    
    for i in range(n):
        lat1, lon1 = waypoints[i]
        lat2, lon2 = waypoints[(i + 1) % n]
        
        if lat1 == lat2 and lon1 == lon2:  # Same waypoint, not a valid edge
            return "no", None
        
        if lat1 == -lat2 and lon1 == 180 - lon2:  # Valid edge
            visited[i] = True
            visited[(i + 1) % n] = True
    
    if all(visited):
        return "yes"
    else:
        for i in range(n):
            if not visited[i]:
                lat, lon = waypoints[i]
                missing_meridian = (lon + 180) % 360 - 180
                break
        return "no", missing_meridian

# Read input
n = int(input())
waypoints = [tuple(map(int, input().split())) for _ in range(n)]

# Determine if it's a valid circumnavigation or find the missing meridian
result, missing_meridian = find_missing_meridian(n, waypoints)
if result == "yes":
    print("yes")
else:
    print("no", int(missing_meridian if missing_meridian % 1 == 0 else missing_meridian + 0.5))