def max_mobsters(N, accusations):
    accusers = {}
    for i in range(1, N + 1):
        accused_by = int(input())
        if accused_by not in accusers:
            accusers[accused_by] = 1
        else:
            accusers[accused_by] += 1
    
    mobsters = max(accusers.values())
    return mobsters

N = int(input())
print(max_mobsters(N, []))