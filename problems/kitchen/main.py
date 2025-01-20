def min_pours(capacities, goal):
    from collections import deque
    
    n = len(capacities)
    initial_state = (capacities[0], [0] * n)
    visited = set([initial_state])
    queue = deque([initial_state])
    
    while queue:
        current, pours = queue.popleft()
        if current == goal:
            return sum(pours)
        
        for i in range(n):
            if pours[i] > 0:
                for j in range(n):
                    if i != j and pours[j] < capacities[j]:
                        new_pours = list(pours)
                        amount = min(capacities[j] - pours[j], pours[i])
                        new_pours[i] -= amount
                        new_pours[j] += amount
                        new_state = (capacities[i], new_pours)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append(new_state)
    return "impossible"

# Read inputs and process each one
import sys
for line in sys.stdin:
    data = list(map(int, line.split()))
    n = data[0]
    capacities = data[1:]
    goal = capacities[-1]
    print(min_pours(capacities, goal))