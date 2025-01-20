n, k = map(int, input().split())
parents = {}
for i in range(1, n + 1):
    c_i, p_i = input().split()
    parents[i] = (c_i, int(p_i))

queries = [input().strip() for _ in range(k)]

# Build the family tree
tree = {1: []}
for i in range(2, n + 1):
    mother_id = parents[i][1]
    if mother_id not in tree:
        tree[mother_id].append(i)
    else:
        tree[mother_id] = [i]

# Count the number of names with each prefix
prefix_count = {}
for name in parents:
    current = name
    while current != 0:
        if tuple(parents[current]) in prefix_count:
            prefix_count[tuple(parents[current])] += 1
        else:
            prefix_count[tuple(parents[current])] = 1
        current = parents[current][1]

# Handle the query strings
for query in queries:
    count = 0
    current = (query[0], 0)
    for i in range(1, len(query) + 1):
        if current in prefix_count:
            count = prefix_count[current]
        current = (query[i], parents[current][1])
    print(count)