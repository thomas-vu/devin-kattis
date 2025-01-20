def can_divide_into_teams(N):
    return "Jebb" if N % 3 == 0 else "Neibb"

# Read input from standard input
N = int(input().strip())
print(can_divide_into_teams(N))