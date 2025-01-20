def max_bridge_length(N, heights):
    stack = []
    left = [0] * N
    right = [0] * N
    
    # Calculate the left limits for each terrace
    for i in range(N):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] + 1 if stack else 0
        stack.append(i)
    
    # Clear the stack for the right limits calculation
    stack.clear()
    
    # Calculate the right limits for each terrace
    for i in range(N - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] - 1 if stack else N - 1
        stack.append(i)
    
    # Calculate the maximum bridge length for each terrace
    max_length = 0
    for i in range(N):
        max_length += (right[i] - left[i] + 1) * heights[i]
    
    return max_length

# Read input from stdin
N = int(input())
heights = list(map(int, input().split()))

# Calculate and print the result
result = max_bridge_length(N, heights)
print(result)