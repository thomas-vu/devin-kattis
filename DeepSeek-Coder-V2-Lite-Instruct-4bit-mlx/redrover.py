def min_chars_to_transmit(route):
    # Count the occurrences of each direction in the route
    north = south = east = west = 0
    for char in route:
        if char == 'N':
            north += 1
        elif char == 'S':
            south += 1
        elif char == 'E':
            east += 1
        elif char == 'W':
            west += 1
    
    # Calculate the minimum number of characters needed for each direction
    min_ns = abs(north - south)
    min_ew = abs(east - west)
    
    # The total number of characters needed is the sum of min(ns, ew) for each pair
    total_chars = max(min_ns, min_ew)
    
    return total_chars

# Read input from stdin
route = input().strip()
print(min_chars_to_transmit(route))