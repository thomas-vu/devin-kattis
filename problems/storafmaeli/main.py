def big_anniversary(n):
    return "Jebb" if n % 10 == 0 else "Neibb"

# Read input from stdin
n = int(input())

# Output the result based on the function
print(big_anniversary(n))