def last_petal(N):
    while N > 1:
        N //= 2
    return N

# Example usage:
print(last_petal(5))  # Output should be 3
print(last_petal(10)) # Output should be 5