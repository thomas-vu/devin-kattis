def find_best_skis(W, vh, N, gates, S, skis):
    min_time = float('inf')
    best_ski = None
    
    for i in range(S):
        ski_speed = skis[i]
        
        for left, right in gates:
            # Calculate the time to travel horizontally and vertically
            horizontal_distance = right - left
            vertical_distance = (right - left) / W
            
            # Calculate the total time required to pass through this pair of gates
            if horizontal_distance <= vh * (vertical_distance + 1):
                total_time = vertical_distance + (horizontal_distance / vh)
                
                # Update the minimum time and best pair of skis if this is better
                if total_time < min_time:
                    min_time = total_time
                    best_ski = ski_speed
    
    return min_time, best_ski

# Read input
W, vh, N = map(int, input().split())
gates = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
skis = [int(input()) for _ in range(S)]

# Sort gates by vertical position
gates.sort(key=lambda x: x[1])

# Find the best pair of skis
min_time, best_ski = find_best_skis(W, vh, N, gates, S, skis)

# Output the result
if best_ski is None:
    print("IMPOSSIBLE")
else:
    print(best_ski)