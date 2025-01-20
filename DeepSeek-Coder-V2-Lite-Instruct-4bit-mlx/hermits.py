def find_quietest_street(N, populations, crossings):
    min_total = float('inf')
    quietest_street = -1
    
    for i in range(N):
        total = populations[i]
        for u, v in crossings:
            if u == i + 1 or v == i + 1:
                total += min(populations[u - 1], populations[v - 1])
        if total < min_total:
            min_total = total
            quietest_street = i + 1
        elif total == min_total and quietest_street > i:
            quietest_street = i + 1
    
    return quietest_street

# Read input
N = int(input())
populations = list(map(int, input().split()))
M = int(input())
crossings = [tuple(map(int, input().split())) for _ in range(M)]

# Find and output the quietest street
print(find_quietest_street(N, populations, crossings))