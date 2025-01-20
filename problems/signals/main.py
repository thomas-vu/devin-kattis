def max_non_crossing_bridges(ports):
    n = len(ports)
    # Create a list to store the maximum number of signals that can be connected without crossing up to each port
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Find the position where ports[i-1] should be placed in the sorted list of right ports
        pos = binary_search(ports[:i], ports[i-1])
        # Update the dp array to include the current port
        dp[i] = max(dp[i-1], 1 + dp[pos])
    
    return dp[-1]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Read input
p = int(input())
ports = [int(input()) for _ in range(p)]

# Output the result
print(max_non_crossing_bridges(ports))