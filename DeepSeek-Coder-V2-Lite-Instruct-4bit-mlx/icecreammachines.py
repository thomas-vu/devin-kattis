def min_cleanings(n, m, k, customers):
    # Initialize the count of cleanings needed for each machine
    cleanings = [0] * k
    
    # Initialize the last cleaned time for each machine
    last_cleaned = [0] * k
    
    # Process each customer in the order they arrive
    for flavor in customers:
        min_cleanings = float('inf')
        # Find the machine that was last cleaned for the desired flavor and is available now
        for i in range(k):
            if last_cleaned[i] + m >= flavor:
                min_cleanings = min(min_cleanings, cleanings[i])
        
        # Assign the customer to the machine that requires the least future cleanings
        if min_cleanings == float('inf'):
            # If no machine is available, use a new one
            min_cleanings = 0
        else:
            # Increment the cleaning count for the chosen machine
            min_cleanings += 1
        
        # Update the cleaning count and last cleaned time for the chosen machine
        cleanings[flavor - 1] = min_cleanings
        last_cleaned[flavor - 1] = flavor
    
    # The total number of cleanings is the sum of all individual machine cleanings
    return sum(cleanings)

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()

n, m, k = int(data[0]), int(data[1]), int(data[2])
customers = [int(data[i]) for i in range(3, n + 3)]

# Output the result
print(min_cleanings(n, m, k, customers))