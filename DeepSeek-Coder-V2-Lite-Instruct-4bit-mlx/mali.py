def solve(N, ABs):
    ABs.sort(key=lambda x: (x[0], -x[1]))
    max_sums = []
    for i in range(N):
        a, b = ABs[i]
        max_sums.append(a + b)
    max_sums.sort()
    result = [max_sums[i // 2] for i in range(N)]
    return result

# Read input
N = int(input())
ABs = [tuple(map(int, input().split())) for _ in range(N)]

# Solve and output the result
results = solve(N, ABs)
for res in results:
    print(res)