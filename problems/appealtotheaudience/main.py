def read_ints():
    return list(map(int, input().split()))

n, k = read_ints()
players_skill = read_ints()
parents = [0] * (n - 1)
for i in range(1, n):
    parents[i - 1] = int(input())

# Build the tree and find leaves
tree = [[] for _ in range(n)]
leaves = []
for i in range(1, n):
    tree[parents[i - 1]].append(i)
for i in range(n):
    if not tree[i]:
        leaves.append(i)

# Sort players by skill in descending order
players_skill.sort(reverse=True)

# Assign players to leaves based on skill
leaf_skills = [0] * n
for i in range(k):
    leaf_idx = leaves[i]
    leaf_skills[leaf_idx] = players_skill[i]

# Calculate the maximal possible happiness
total_happiness = 0
for i in range(n):
    for child in tree[i]:
        total_happiness += max(leaf_skills[child], leaf_skills[i])

print(total_happiness)