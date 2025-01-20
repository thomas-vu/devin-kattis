def shortest_representation(buses):
    buses.sort()
    result = []
    i = 0
    while i < len(buses):
        start = buses[i]
        end = start
        while i + 1 < len(buses) and buses[i + 1] == end + 1:
            end = buses[i + 1]
            i += 1
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")
        i += 1
    return ' '.join(result)

# Read input
N = int(input().strip())
buses = list(map(int, input().strip().split()))

# Get the shortest representation
shortest = shortest_representation(buses)
print(shortest)