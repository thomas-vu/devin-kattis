# Solution to the All Just A Dream problem

import sys
from collections import deque

# Read number of events, dreams, and scenarios
n = int(sys.stdin.readline().strip())
events = []
dreams = deque()
scenarios = []

# Read each line and classify it as event, dream, or scenario
for _ in range(n):
    line = sys.stdin.readline().strip()
    if line.startswith('E'):
        events.append(line[2:])
    elif line.startswith('D'):
        dreams.appendleft(int(line[2:]))
    elif line.startswith('S'):
        scenarios.append([x for x in line[2:].split() if x != '!'])

# Process each scenario
results = []
current_dream_index = 0
for scenario in scenarios:
    possible = True
    dream_count = 0
    for event in scenario:
        if event[0] == '!':
            # Check if the negated event has happened
            if event[1:] not in events:
                possible = False
                break
        else:
            # Check if the event has happened
            if event not in events and (current_dream_index < len(dreams) and dreams[current_dream_index] > 0):
                current_dream_index += 1
                dream_count += 1
            else:
                possible = False
                break
    if not possible:
        results.append("Plot Error")
    elif dream_count > 0 and current_dream_index < len(dreams):
        results.append(f"{dream_count} Just A Dream")
    else:
        results.append("Yes")

# Output the results
for result in results:
    print(result)