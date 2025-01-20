def max_executives(N, bananas):
    # Sort the list of bananas in ascending order
    sorted_bananas = sorted(bananas)
    
    # Initialize the maximum number of executives that can be rewarded
    max_exec = 0
    
    # Use two pointers to find the maximum number of executives that can be rewarded
    left = 0
    right = sum(bananas)
    
    for i in range(N):
        left += sorted_bananas[i]
        right -= sorted_bananas[i]
        
        # Check if the distribution is fair
        if left >= right:
            max_exec = i + 1
    
    return max_exec

# Read input from the user
N = int(input())
bananas = list(map(int, input().split()))

# Output the maximum number of executives that can be rewarded
print(max_executives(N, bananas))