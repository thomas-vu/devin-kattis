def find_initial_pattern(w, h, final_pattern):
    def count_filled_neighbors(x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and final_pattern[nx][ny] == '#':
                    count += 1
        return count
    
    def next_state(x, y):
        filled_neighbors = count_filled_neighbors(x, y)
        if final_pattern[x][y] == '#':
            return '#' if filled_neighbors % 2 == 1 else '.'
        else:
            return '#' if filled_neighbors % 2 == 0 else '.'
    
    def flip_one_cell(x, y):
        if final_pattern[x][y] == '#':
            return '.'
        else:
            return '#'
    
    def possible_initial_patterns(x, y):
        if final_pattern[x][y] == '#':
            return [flip_one_cell(x, y)]
        else:
            return ['#', '.']
    
    def is_valid(pattern):
        for x in range(h):
            for y in range(w):
                if pattern[x][y] == '#':
                    filled_neighbors = count_filled_neighbors(x, y)
                    if filled_neighbors % 2 != 0:
                        return False
        return True
    
    def expand_pattern(pattern):
        expanded = [['.' for _ in range(w + 2)] for _ in range(h + 2)]
        for x in range(h):
            for y in range(w):
                expanded[x + 1][y + 1] = pattern[x][y]
        return expanded
    
    def shrink_pattern(pattern):
        start_x = h
        end_x = -1
        start_y = w
        end_y = -1
        for x in range(h):
            for y in range(w):
                if pattern[x][y] == '#':
                    start_x = min(start_x, x)
                    end_x = max(end_x, x)
                    start_y = min(start_y, y)
                    end_y = max(end_y, y)
        return [row[start_y:end_y + 1] for row in pattern[start_x:end_x + 1]]
    
    def generate_patterns(pattern):
        for x in range(h):
            for y in range(w):
                for state in possible_initial_patterns(x, y):
                    new_pattern = [row[:] for row in pattern]
                    new_pattern[x][y] = state
                    if is_valid(new_pattern):
                        yield new_pattern
    
    min_area = float('inf')
    best_pattern = None
    for pattern in generate_patterns(final_pattern):
        expanded_pattern = expand_pattern(pattern)
        if is_valid(expanded_pattern):
            shrunk_pattern = shrink_pattern(expanded_pattern)
            area = len(shrunk_pattern) * len(shrunk_pattern[0])
            if area < min_area:
                min_area = area
                best_pattern = shrunk_pattern
    
    return best_pattern

# Read input
w, h = map(int, input().split())
final_pattern = [list(input().strip()) for _ in range(h)]

# Find and print the initial pattern
initial_pattern = find_initial_pattern(w, h, final_pattern)
for row in initial_pattern:
    print(''.join(row))