import math

def calculate_zipline_lengths(w, g, h, r):
    # Minimum length of the cable: straight line between the two poles
    min_length = math.sqrt(w**2 + (g - h)**2)
    
    # Maximum height the rider can reach above the cable at the midpoint
    max_height = math.sqrt((w / 2)**2 + r**2)
    
    # Maximum length of the cable: sum of the segments from each pole to the rider at the midpoint
    max_length = math.sqrt((w / 2)**2 + (g - h + max_height)**2)
    
    return min_length, max_length

# Read number of ziplines from input
n = int(input().strip())
results = []
for _ in range(n):
    w, g, h, r = map(int, input().strip().split())
    min_length, max_length = calculate_zipline_lengths(w, g, h, r)
    results.append((min_length, max_length))

# Output the results with the required precision
for min_len, max_len in results:
    print("{:.8f} {:.8f}".format(min_len, max_len))