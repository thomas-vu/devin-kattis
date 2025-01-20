def find_crates(n):
    for height in range(2, 100):
        for width in range(2, 100):
            if height * width == n:
                return f"{height}x{width}"
    return "impossible"

# Read input from stdin
n = int(input().strip())
print(find_crates(n))