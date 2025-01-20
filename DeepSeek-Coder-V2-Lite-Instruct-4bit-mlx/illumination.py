def can_light_all_lamps(n, r, k, lamps):
    from itertools import combinations
    
    # Create a list to store the rows and columns where lamps are placed
    row_positions = set()
    col_positions = set()
    
    # Populate the sets with lamp positions
    for i, j in lamps:
        row_positions.add(i)
        col_positions.add(j)
    
    # Check if it's possible to light all lamps
    for row in range(1, n + 1):
        if row not in row_positions:
            # Check for possible placements of lamps in this row
            possible_row_placements = set(range(max(1, row - r), min(n + 1, row + r + 1))
            if not possible_row_placements.intersection(row_positions):
                # No lamps in the row, check columns for placement
                possible_col_placements = set(range(max(1, col - r), min(n + 1, col + r + 1))
                if not possible_col_placements.intersection(col_positions):
                    return 0
    
    for col in range(1, n + 1):
        if col not in col_positions:
            # Check for possible placements of lamps in this column
            possible_col_placements = set(range(max(1, col - r), min(n + 1, col + r + 1))
            if not possible_col_placements.intersection(col_positions):
                # No lamps in the column, check rows for placement
                possible_row_placements = set(range(max(1, row - r), min(n + 1, row + r + 1))
                if not possible_row_placements.intersection(row_positions):
                    return 0
    
    return 1

# Read input
n, r, k = map(int, input().split())
lamps = [tuple(map(int, input().split())) for _ in range(k)]

# Output the result
print(can_light_all_lamps(n, r, k, lamps))