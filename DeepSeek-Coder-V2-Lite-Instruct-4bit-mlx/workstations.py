def calculate_unlockings(n, m, researchers):
    events = []
    for a, s in researchers:
        events.append((a, 1))  # Arrival of a researcher
        events.append((a + s, -1))  # Departure of a researcher
    
    events.sort()
    
    current_unlocked = 0
    max_unlocked = 0
    workstation_count = 0
    
    for time, change in events:
        current_unlocked += change
        if current_unlocked > max_unlocked:
            max_unlocked = current_unlocked
            workstation_count += 1
    
    initial_unlockings = sum(1 for a, s in researchers)
    saved_unlockings = initial_unlockings - max_unlocked
    
    return saved_unlockings

# Read input
n, m = map(int, input().split())
researchers = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the result
result = calculate_unlockings(n, m, researchers)
print(result)