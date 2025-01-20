def max_ski_lifts(n, pylons):
    from collections import defaultdict
    
    # Grouping the pylons by their x-coordinates and y-coordinates
    x_dict = defaultdict(list)
    y_dict = defaultdict(list)
    
    for x, y, a in pylons:
        x_dict[x].append((y, a))
        y_dict[y].append((x, a))
    
    # Counting the number of unique x-coordinates and y-coordinates
    unique_xs = len(x_dict)
    unique_ys = len(y_dict)
    
    # If there are more than 2 unique y-coordinates, it's impossible to satisfy the conditions
    if unique_ys > 2:
        return -1
    
    # Counting the number of one-way and two-way pylons
    one_way = sum(1 for _, a in x_dict.values() if a == 1)
    two_way = sum(1 for _, a in x_dict.values() if a == 2)
    
    # If there are more one-way pylons than two-way ones, it's impossible to connect them properly
    if one_way > 0 and two_way == 0:
        return -1
    
    # Counting the number of connections possible for each two-way pylon
    connections = [0] * n
    for y in range(unique_ys):
        if len(y_dict[y]) == 2:
            connections[y] = 1
    
    # Calculating the maximum number of ski lifts
    max_lifts = sum(connections) + min(one_way, two_way)
    
    return max_lifts

# Reading input
n = int(input())
pylons = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_ski_lifts(n, pylons))