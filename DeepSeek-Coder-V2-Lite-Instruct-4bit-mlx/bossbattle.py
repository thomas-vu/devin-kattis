def min_bombs_to_defeat_boss(n):
    # The minimum number of bombs needed is the maximum between one bomb and two adjacent pillars.
    return (n + 1) // 2

# Read the number of pillars from input
n = int(input().strip())

# Output the minimum number of bombs needed
print(min_bombs_to_defeat_boss(n))