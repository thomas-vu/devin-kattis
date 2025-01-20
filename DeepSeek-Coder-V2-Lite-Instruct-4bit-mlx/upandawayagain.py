n, x, t = map(int, input().split())
h = list(map(int, input().split()))
d = list(map(int, input().split()))

# Initialize the minimum time to a large value
min_time = float('inf')

# Iterate through all possible starting points to find the minimum time
for start in range(n):
    if h[start] <= h[x-1]:  # Check if the starting mountain can be reached
        time = 0
        current_mountain = start
        while h[current_mountain] < h[x-1]:  # Traverse the ski lifts
            for next_mountain in range(n):
                if h[next_mountain] <= h[current_mountain] + d[current_mountain]:
                    time += t  # Add the time for each ski lift
                    current_mountain = next_mountain
        min_time = min(min_time, time)  # Update the minimum time if a better path is found

# Output the result
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)