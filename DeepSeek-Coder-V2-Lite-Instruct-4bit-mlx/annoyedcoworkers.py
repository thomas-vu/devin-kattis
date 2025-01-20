def min_max_annoyance(h, c, coworkers):
    max_annoyance = float('inf')
    
    for i in range(len(coworkers)):
        current_annoyance = 0
        for j in range(len(coworkers)):
            if i != j:
                current_annoyance += min(h, (coworkers[j][0] + coworkers[j][1] * h) // coworkers[j][1])
        max_annoyance = min(max_annoyance, max((coworkers[i][0] + coworkers[i][1] * h) // coworkers[i][1]))
    
    return max_annoyance

# Read input
h, c = map(int, input().split())
coworkers = [list(map(int, input().split())) for _ in range(c)]

# Calculate and output the result
print(min_max_annoyance(h, c, coworkers))