def pour_drinks(n, glasses):
    max_glass = max(glasses)
    min_glass = min(glasses)
    
    if (max_glass - min_glass) % 2 != 0:
        return -1
    
    pourings = []
    while max_glass != min_glass:
        for i in range(n):
            if glasses[i] > min_glass:
                diff = glasses[i] - min_glass
                pourings.append((i + 1, (i + 2) % (n + 1)))
                glasses[i] -= diff
                glasses[(i + 1) % n] += diff
        max_glass = max(glasses)
        min_glass = min(glasses)
    
    print(len(pourings))
    for p in pourings:
        print(*p)

# Read input
n = int(input())
glasses = list(map(int, input().split()))

# Solve the problem
pour_drinks(n, glasses)