def solve(N):
    counter = 0
    for i in range(N - 1, 0, -1):
        counter += 1
        if N % i == 0:
            break
    return counter

# Read input from stdin
N = int(input().strip())
print(solve(N))