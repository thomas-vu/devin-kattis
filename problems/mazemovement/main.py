import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_max_people(rooms):
    adj = defaultdict(list)
    for room in rooms:
        for other_room in rooms:
            if room != other_room and gcd(room, other_room) > 1:
                adj[room].append(other_room)
    
    max_people = 0
    for room in rooms:
        visited = set()
        stack = [room]
        current_flow = float('inf')
        
        while stack:
            r = stack.pop()
            if r in visited:
                continue
            visited.add(r)
            for neighbor in adj[r]:
                if neighbor not in visited:
                    stack.append(neighbor)
            current_flow = min(current_flow, r)
        
        max_people = max(max_people, current_flow)
    
    return max_people

# Read input
n = int(input())
rooms = [int(input()) for _ in range(n)]

# Find and print the result
print(find_max_people(rooms))