def min_rounds(m):
    rounds = 0
    while True:
        if pow(2, rounds, m) == 1:
            return rounds
        rounds += 1

# Read input from stdin
m = int(input().strip())
print(min_rounds(m))