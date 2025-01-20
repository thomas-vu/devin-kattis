def who_wins(N):
    if N % 2 == 0:
        return "Bob"
    else:
        return "Alice"

# Read the number of stones from input
N = int(input().strip())
# Determine and print the winner
print(who_wins(N))