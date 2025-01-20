# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Create adjacency list
adj_list = [[] for _ in range(n + 1)]
for v, w in edges:
    adj_list[v].append(w)
    adj_list[w].append(v)

# Determine if a U-turn is possible from the entrance v of street S
def can_u_turn(v, w):
    for neighbor in adj_list[w]:
        if neighbor == v:  # Check if there's a direct path back to the starting location
            return True
    return False

# Determine dead-ends
dead_ends = []
for v, w in edges:
    if not can_u_turn(v, w):  # If a U-turn is not possible
        dead_ends.append((v, w))

# Output the result
print(len(dead_ends))
for v, w in sorted(dead_ends):
    print(v, w)