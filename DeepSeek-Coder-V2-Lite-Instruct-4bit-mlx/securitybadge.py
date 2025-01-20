def read_ints():
    return list(map(int, input().split()))

N, L, B = read_ints()
S, D = read_ints()
locks = [tuple(read_ints()) for _ in range(L)]
badge_numbers = read_ints()

# Create adjacency lists for both directions of each lock
adj_list = [[] for _ in range(N + 1)]
reverse_adj_list = [[] for _ in range(N + 1)]
for a, b, x, y in locks:
    adj_list[a].append((b, x, y))
    reverse_adj_list[b].append((a, x, y))

# Function to count valid badge numbers for a given adjacency list and bounds
def count_valid_badge_numbers(adj_list, start, end, x, y):
    count = 0
    for badge in range(x, y + 1):
        if can_reach(adj_list, start, end, badge):
            count += 1
    return count

# Helper function to check if a badge can reach the destination using DFS
def can_reach(adj_list, start, end, badge):
    visited = set()
    stack = [start]
    while stack:
        room = stack.pop()
        if room == end:
            return True
        for neighbor, lower_bound, upper_bound in adj_list[room]:
            if lower_bound <= badge <= upper_bound and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return False

# Calculate the number of valid badge numbers for S to D using both adjacency lists
valid_badge_numbers = count_valid_badge_numbers(adj_list, S, D, 1, B) + count_valid_badge_numbers(reverse_adj_list, S, D, 1, B)
print(valid_badge_numbers)