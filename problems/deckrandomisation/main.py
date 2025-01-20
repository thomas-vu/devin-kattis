from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def cycle_length(n, perm):
    visited = [False] * n
    cycles = []
    for i in range(n):
        if not visited[i]:
            cycle = []
            while not visited[i]:
                visited[i] = True
                cycle.append(i)
                i = perm[i] - 1
            cycles.append(cycle)
    return cycles

def min_shuffles(n, alice_perm, bob_perm):
    alice_cycles = cycle_length(n, alice_perm)
    bob_cycles = cycle_length(n, bob_perm)
    
    lcm_val = 1
    for cycle in alice_cycles:
        lcm_val = lcm(lcm_val, len(cycle))
    for cycle in bob_cycles:
        lcm_val = lcm(lcm_val, len(cycle))
    
    return min(lcm_val, 10**12)

# Read input
n = int(input())
alice_perm = list(map(int, input().split()))
bob_perm = list(map(int, input().split()))

# Calculate and print the result
result = min_shuffles(n, alice_perm, bob_perm)
print(result)