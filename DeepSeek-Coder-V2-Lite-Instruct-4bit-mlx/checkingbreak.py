def is_valid_solution(a, b, c, m, chips, parts):
    # Check if the number of parts matches the number of chocolate chips
    if len(parts) != m:
        return 'NO'
    
    # Create a dictionary to keep track of the parts and their positions
    part_positions = {}
    
    # Parse the parts and store their coordinates in a dictionary
    for part in parts:
        x, y, z, u, v, w = part
        key = ((x, u), (y, v), (z, w))
        part_positions[key] = True
    
    # Check if each chocolate chip is in exactly one part
    used_positions = set()
    for i, (x, y, z) in enumerate(chips):
        key = ((x, x), (y, y), (z, z))
        if key not in part_positions or key in used_positions:
            return 'NO'
        used_positions.add(key)
    
    # Check if the volume of the intersection of any two parts is zero
    for key1 in part_positions:
        for key2 in part_positions:
            if key1 != key2 and (set(key1) & set(key2)):
                return 'NO'
    
    return 'YES'

# Read input until -1 is encountered
while True:
    line = list(map(int, input().split()))
    if line[0] == -1:
        break
    
    a, b, c, m = line
    chips = [tuple(map(int, input().split())) for _ in range(m)]
    parts = [list(map(int, input().split())) for _ in range(m)]
    
    result = is_valid_solution(a, b, c, m, chips, parts)
    print(result)