import sys
from bisect import insort, bisect_left

# Initialize the holding area list and result list
holding = []
results = []

for line in sys.stdin:
    if line.strip() == '#':
        # If the holding area is empty, send the smallest cookie
        if not holding:
            results.append(1)  # Assuming the smallest cookie is 1 nm if empty
        else:
            n = len(holding)
            # Send the cookie at position (n + 1) // 2 if n is odd, or n // 2 if n is even
            if n % 2 == 1:
                median_index = (n + 1) // 2
            else:
                median_index = n // 2
            results.append(holding[median_index - 1])
    else:
        # Add the new cookie diameter to the holding area
        d = int(line.strip())
        insort(holding, d)

# Output the results
for result in results:
    print(result)