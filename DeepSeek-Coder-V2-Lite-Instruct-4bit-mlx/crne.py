def max_pieces(N):
    return (N + 1) * (N + 2) // 2

# Read input from stdin
N = int(input().strip())
print(max_pieces(N))