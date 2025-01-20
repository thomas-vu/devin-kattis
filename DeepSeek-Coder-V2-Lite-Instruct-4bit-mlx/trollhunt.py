b, k, g = map(int, input().split())

# Calculate the number of groups and the size of each group
groups = k // g
remaining_knights = k % g
if remaining_knights == 0:
    groups -= 1

# Calculate the number of days until the troll is caught
days = (b - 1) // groups
print(days)