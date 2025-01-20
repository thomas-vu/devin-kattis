def find_optimal_cut(n, markers):
    from collections import defaultdict
    
    # Initialize counters for each gene type
    start_end_count = defaultdict(int)
    
    # Count the number of starts and ends for each gene type
    for marker in markers:
        _, gene_type = marker.split()
        if marker[0] == 's':
            start_end_count[(gene_type, 'start')] += 1
        else:
            start_end_count[(gene_type, 'end')] += 1
    
    # Initialize variables to track the maximum nesting count and position
    max_nesting = 0
    optimal_position = 0
    
    # Calculate the number of properly nested gene types for each possible cut
    nesting_count = 0
    for i in range(n):
        if markers[i][0] == 's':
            nesting_count += start_end_count[(markers[i].split()[1], 'end')]
        elif markers[i][0] == 'e':
            nesting_count -= start_end_count[(markers[i].split()[1], 'start')]
        
        # Update the maximum nesting count and position if necessary
        if nesting_count > max_nesting:
            max_nesting = nesting_count
            optimal_position = i + 1
    
    return optimal_position, max_nesting

# Read input
n = int(input())
markers = [input().strip() for _ in range(n)]

# Find the optimal cut position and maximum nesting count
p, m = find_optimal_cut(n, markers)

# Output the result
print(p, m)