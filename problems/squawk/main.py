def count_squawks(n, m, s, t, links):
    # Create adjacency list for the graph
    adj_list = [[] for _ in range(n)]
    for x, y in links:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    # Initialize the number of squawks at each user
    squawks = [0] * n
    squawks[s] = 1
    
    # Simulate the spread of squawks over time
    for _ in range(t):
        new_squawks = [0] * n
        for user in range(n):
            new_squawks[user] += squawks[user]
            for neighbor in adj_list[user]:
                new_squawks[neighbor] += squawks[user]
        squawks = new_squawks
    
    # Sum the total number of squawks at time t
    return sum(squawks)

# Read input
n, m, s, t = map(int, input().split())
links = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(count_squawks(n, m, s, t, links))