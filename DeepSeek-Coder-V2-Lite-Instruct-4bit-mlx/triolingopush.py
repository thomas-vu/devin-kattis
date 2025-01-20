MOD = 10**9 + 7

def calculate_notifications(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    
    prev, curr = 1, 2
    for _ in range(3, N + 1):
        next_val = (curr + prev + 1) % MOD
        prev, curr = curr, next_val
    
    return curr

# Read input
N = int(input())
print(calculate_notifications(N))