n, lph = map(int, input().split())
problems = [int(input()) for _ in range(n)]

# Sort the problems by the number of lines of code required to solve them
problems.sort()

# Initialize variables for the binary search algorithm
left, right = 0, n

# Binary search to find the maximum number of problems that can be solved within the time limit
while left < right:
    mid = (left + right + 1) // 2
    total_loc = sum(problems[:mid])
    
    # Check if the best team can solve all problems within 5 hours
    if total_loc <= mid * lph:
        left = mid
    else:
        right = mid - 1

# Output the result
print(left)