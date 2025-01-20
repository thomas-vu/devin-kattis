n = int(input())
lanes = int(input())
total_cells = n * lanes
empty_cells = 0

for _ in range(lanes):
    cells = input()
    for cell in cells:
        if cell == '.':
            empty_cells += 1

proportion = empty_cells / total_cells
print("{:.5f}".format(proportion))