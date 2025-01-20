def find_shortest_substring(N, K, R, DNA, requirements):
    # Convert nucleobases to their respective indices in the list
    D = [int(x) for x in DNA]
    
    # Initialize the minimum length of the substring to a large number
    min_length = float('inf')
    
    # Iterate over all possible starting points of the substring
    for start in range(N):
        # Initialize counters for each nucleobase required
        counts = [0] * K
        
        # Count the nucleobases in the current substring
        for end in range(start, N):
            # Update the count of the current nucleobase
            counts[D[end]] += 1
            
            # Check if the current substring satisfies all requirements
            satisfied = True
            for b, q in requirements:
                if counts[b] < q:
                    satisfied = False
                    break
            
            # If the substring satisfies all requirements, update min_length
            if satisfied:
                min_length = min(min_length, end - start + 1)
                
            # If we have satisfied all requirements and the substring is not shorter, break
            if min_length == R:
                return min_length
    
    # If no valid substring was found, return "impossible"
    if min_length == float('inf'):
        return "impossible"
    
    return min_length

# Read input
N, K, R = map(int, input().split())
DNA = input().split()
requirements = [tuple(map(int, input().split())) for _ in range(R)]

# Output the result
print(find_shortest_substring(N, K, R, DNA, requirements))