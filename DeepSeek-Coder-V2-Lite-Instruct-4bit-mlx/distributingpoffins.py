def min_diff(N, M):
    base = M // N
    remainder = M % N
    
    min_poffins = base
    max_poffins = base + 1
    
    min_diff = max_poffins - min_poffins
    
    if remainder == 0:
        return min_diff
    else:
        additional = N - remainder
        min_poffins -= additional // N
        max_poffins -= (additional + 1) // N
        return min(min_diff, max_poffins - min_poffins)

# Read input
N, M = map(int, input().split())
print(min_diff(N, M))