def is_safe(N):
    # If N is even, Peach will be caught because Powder can always match her pace.
    return "No" if N % 2 == 0 else "Yes"

# Read the number of castles from input
N = int(input())

# Output the result
print(is_safe(N))