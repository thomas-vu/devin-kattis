import sys
input = sys.stdin.readline

# Read the number of problems (N) and queries (Q)
N, Q = map(int, input().split())
# Read the difficulties of the problems
D_i = list(map(int, input().split()))

# Initialize the result list for storing discarded difficulties
result = []

for _ in range(Q):
    T, D = map(int, input().split())
    
    if T == 1:
        # Discard problems strictly harder than D
        while D_i and D_i[-1] > D:
            result.append(D_i.pop())
    elif T == 2:
        # Discard problems not harder than D
        while D_i and D_i[0] <= D:
            result.append(D_i.pop(0))
    
    # Output the discarded difficulties or -1 if no problem was found
    print(-1) if not D_i else print(D_i[-1])