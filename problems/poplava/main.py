def find_histogram(N, X):
    # Check if the given capacity is achievable with N columns
    max_height = X + N  # The maximum possible height of the histogram with water
    
    # If N is less than or equal to X, it's impossible to achieve the capacity
    if N <= X:
        return -1
    
    # Generate a valid histogram configuration with heights in the range [1, N]
    heights = list(range(N, 0, -1))
    
    # Calculate the capacity of this initial histogram configuration
    current_capacity = sum(heights[i] + heights[i+1] for i in range(N-1))
    
    # If the initial configuration meets the required capacity, return it
    if current_capacity == X:
        return heights
    
    # Otherwise, try to adjust the heights to achieve the desired capacity X
    for i in range(N):
        for j in range(i+1, N):
            # Swap the heights at positions i and j
            heights[i], heights[j] = heights[j], heights[i]
            
            # Recalculate the new capacity
            new_capacity = sum(heights[k] + heights[k+1] for k in range(N-1))
            
            # Check if the new configuration meets the required capacity X
            if new_capacity == X:
                return heights
            
            # Swap back to the original configuration if not met
            heights[i], heights[j] = heights[j], heights[i]
    
    # If no configuration meets the required capacity, return -1
    return -1

# Read input
N, X = map(int, input().split())

# Get the histogram configuration and print it
result = find_histogram(N, X)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))