def quadkey_to_coords(quadkey):
    zoom = len(quadkey)
    x, y = 0, 0
    
    for i in range(zoom):
        mask = 1 << (zoom - i - 1)
        if quadkey[i] == '1':
            x |= mask
        elif quadkey[i] == '2':
            y |= mask
        elif quadkey[i] == '3':
            x |= mask
            y |= mask
    
    return zoom, x, y

# Read input
quadkey = input().strip()

# Convert quadkey to coordinates and print the result
zoom, x, y = quadkey_to_coords(quadkey)
print(zoom, x, y)