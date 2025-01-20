def find_house_order(n, directions):
    houses = list(range(1, n + 1))
    for i in range(n - 2, -1, -1):
        if directions[i] == 'R':
            houses[i], houses[i + 1] = houses[i + 1], houses[i]
    return houses

# Read input
n = int(input().strip())
directions = input().strip()

# Get the lexicographically earliest order
order = find_house_order(n, directions)

# Output the result
for house in order:
    print(house)