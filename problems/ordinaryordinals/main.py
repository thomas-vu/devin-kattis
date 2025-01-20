def f(N, M):
    if N == 0:
        return 1 % M
    
    # Initialize the set representation of N
    represent = [0] * (N + 1)
    represent[0] = 0
    
    for i in range(1, N + 1):
        represent[i] = (1 << i) - 1
    
    # Calculate the number of characters required for each set representation
    total_chars = 0
    for i in range(N + 1):
        total_chars += len(bin(represent[i])) - 2 + (N - i) * (len(bin(represent[i])) - 2)
    
    return total_chars % M

# Read input
N, M = map(int, input().split())
print(f(N, M))