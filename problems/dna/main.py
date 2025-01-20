def min_mutations(N, sequence):
    # Count the number of 'A's and 'B's in the sequence
    count_a = sequence.count('A')
    count_b = sequence.count('B')
    
    # If all characters are 'A', no mutations are needed
    if count_a == N:
        return 0
    
    # If all characters are 'B', we need to flip the entire sequence once
    if count_b == N:
        return 1
    
    # If there are both 'A's and 'B's, we can use the minimum number of flips
    # to convert all characters to 'A' by flipping subsegments
    min_flips = float('inf')
    
    # Check each possible prefix length from 1 to N
    for k in range(1, N + 1):
        # Count the number of mismatches at each position for a subsegment of length k
        mismatches = 0
        for i in range(N):
            if sequence[i] != (sequence[(i + k) % N]):
                mismatches += 1
        
        # The minimum number of mutations for this subsegment length k
        min_flips = min(min_flips, mismatches)
    
    # The total number of mutations is the minimum number of mismatches plus 1 flip
    return min_flips + 1

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
sequence = data[1]

# Output the result
print(min_mutations(N, sequence))