def count_bell_tolls(creatures):
    bell_count = 0
    while 'O' in creatures:
        new_creatures = []
        for creature in creatures:
            if creature == 'O':
                new_creatures.append('Z')
            else:
                new_creatures.append('O')
        creatures = new_creatures
        bell_count += 1
    return bell_count

# Read input
N = int(input().strip())
creatures = [input().strip() for _ in range(N)]

# Output the result
print(count_bell_tolls(creatures))