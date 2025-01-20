N, K = map(int, input().split())
jumps = list(map(int, input().split()))
Q = int(input())
special_parts = [list(map(int, input().split())) for _ in range(Q)]

# Initialize the array with zeros
seq = [0] * N

# Process each jump call
for jump in jumps:
    i = 0
    while i < N:
        seq[i] += 1
        i += jump

# Compute the sum for each special part
for L, R in special_parts:
    print(sum(seq[L:R+1]))