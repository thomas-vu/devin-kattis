def min_rooms(minions):
    intervals = []
    for minion in minions:
        intervals.append((minion[0], 1))
        intervals.append((minion[1] + 1, -1))
    
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    current_rooms = 0
    max_rooms = 0
    
    for interval in intervals:
        current_rooms += interval[1]
        max_rooms = max(max_rooms, current_rooms)
    
    return max_rooms

# Read input
N = int(input())
minions = [tuple(map(int, input().split())) for _ in range(N)]

# Output the result
print(min_rooms(minions))