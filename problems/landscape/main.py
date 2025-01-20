def apply_operation(landscape, operation, x1, x2):
    if operation == 'R':
        for i in range(x1 - 1, x2):
            landscape[i] += 1
    elif operation == 'D':
        for i in range(x1 - 1, x2):
            landscape[i] -= 1
    elif operation == 'H':
        for i in range(x1 - 1, x2):
            landscape[i] += (i - x1 + 1)
        for i in range(x2, n):
            landscape[i] += (x2 - i)
    elif operation == 'V':
        for i in range(x1 - 1, x2):
            landscape[i] -= (i - x1 + 1)
        for i in range(x2, n):
            landscape[i] -= (x2 - i)
    return landscape

n, k = map(int, input().split())
landscape = [0] * n
for _ in range(k):
    operation, x1, x2 = input().split()
    x1, x2 = int(x1), int(x2)
    landscape = apply_operation(landscape, operation, x1, x2)

for height in landscape:
    print(height)