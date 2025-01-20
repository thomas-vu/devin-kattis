def min_difference(packages):
    n = len(packages)
    total_sum = sum(packages)
    min_diff = float('inf')
    best_assignment = []
    
    for mask in range(1 << n):
        sumA = 0
        sumB = 0
        assignment = []
        
        for j in range(n):
            if mask & (1 << j):
                sumA += packages[j]
                assignment.append((packages[j], 'A'))
            else:
                sumB += packages[j]
                assignment.append((packages[j], 'B'))
        
        diff = abs(sumA - sumB)
        if diff < min_diff:
            min_diff = diff
            best_assignment = assignment.copy()
    
    return best_assignment

while True:
    N = int(input())
    if N == 0:
        break
    
    packages = list(map(int, input().split()))
    assignment = min_difference(packages)
    
    for package in assignment:
        print(f"{package[0]}-{package[1]}", end=' ')
    print()