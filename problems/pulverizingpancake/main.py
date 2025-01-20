def min_pulverizing_pancakes(N, M, pokemon_columns):
    count = 0
    i = 0
    while i < N:
        if pokemon_columns[i] == '1':
            count += 1
            i += 3
        else:
            i += 1
    return count

# Read input
N, M = map(int, input().split())
pokemon_columns = input()

# Calculate and output the result
print(min_pulverizing_pancakes(N, M, pokemon_columns))