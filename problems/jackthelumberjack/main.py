def max_trees(N, species):
    max_harvest = 0
    for S, B, Y, I in species:
        current_population = S
        year = 0
        while year <= B + Y:
            if year >= B and year < B + Y:
                current_population += I
            else:
                current_population -= I
            if year >= B and year < B + Y:
                max_harvest = max(max_harvest, current_population)
            year += 1
    return max_harvest

# Read input
N = int(input())
species = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(max_trees(N, species))