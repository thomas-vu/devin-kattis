def can_attend_all(lectures, travel_times, start_time):
    # Create a graph where each node represents a campus and edges represent travel times
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for (i, j, t) in travel_times:
        graph[i].append((j, t))
        graph[j].append((i, t))
    
    # Use BFS to find the maximum number of lectures that can be attended
    max_lectures = 0
    
    for start in range(len(graph)):
        visited = [False] * len(graph)
        queue = deque([(start, 0)])  # (current_campus, current_time)
        lectures_attended = set()
        
        while queue:
            current_campus, current_time = queue.popleft()
            
            if not visited[current_campus]:
                visited[current_campus] = True
                
                # Check all lectures at the current campus
                for lecture in lectures:
                    if lecture[0] == current_campus and start_time <= lecture[1] <= current_time:
                        lectures_attended.add((lecture[0], lecture[1]))
                
                # Add all adjacent campuses with their travel times
                for neighbor, time in graph[current_campus]:
                    if current_time + time <= 8600000:  # Check if the next lecture can be attended
                        queue.append((neighbor, current_time + time))
                
                # Update the start time for the next lecture to the end of the current lecture
                start_time = min(lectures_attended, key=lambda x: x[1])[1] if lectures_attended else start_time
        
        max_lectures = max(max_lectures, len(lectures_attended))
    
    return max_lectures

# Read input and process each test case
import sys
input = sys.stdin.read
data = input().split()
index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    C = int(data[index])
    index += 1
    L = int(data[index])
    index += 1
    travel_times = []
    
    for _ in range(C * (C - 1) // 2):
        i = int(data[index])
        j = int(data[index + 1])
        t = int(data[index + 2])
        index += 3
        travel_times.append((i, j, t))
    
    lectures = []
    for _ in range(L):
        C_l = int(data[index])
        S_l = int(data[index + 1])
        E_l = int(data[index + 2])
        index += 3
        lectures.append((C_l, S_l, E_l))
    
    result = can_attend_all(lectures, travel_times, 0)
    results.append(result)

# Output the results
for result in results:
    print(result)