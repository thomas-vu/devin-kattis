def min_crossings(path):
    crossings = 0
    for char in path:
        if char == 'N':
            crossings += 1
        elif char == 'S':
            if crossings > 0:
                crossings -= 1
            else:
                crossings += 1
        elif char == 'B':
            if crossings > 0:
                crossings -= 1
            else:
                crossings += 1
    return crossings * 2

# Read input from stdin
path = input().strip()
print(min_crossings(path))