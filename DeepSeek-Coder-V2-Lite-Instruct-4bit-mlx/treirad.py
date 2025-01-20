def count_triple_numbers(N):
    def is_nice_triplet(a, b, c):
        return a * b * c < N
    
    count = 0
    for a in range(1, int(N**0.5) + 1):
        for b in range(a, a + 2):
            c = b + 1
            if is_nice_triplet(a, b, c):
                count += 1
    return count

# Read input from stdin
N = int(input().strip())
print(count_triple_numbers(N))