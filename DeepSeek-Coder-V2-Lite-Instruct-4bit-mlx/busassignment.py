def min_bus_capacity(n, stops):
    max_people = 0
    current_people = 0
    
    for a, b in stops:
        current_people += b - a
        max_people = max(max_people, current_people)
    
    return max_people

# Read input
n = int(input())
stops = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the minimum bus capacity
print(min_bus_capacity(n, stops))