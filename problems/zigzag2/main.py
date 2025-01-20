def longest_zigzag_subsequence(nums):
    if len(nums) <= 1:
        return len(nums)
    
    up = [0] * len(nums)
    down = [0] * len(nums)
    
    up[0], down[0] = 1, 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]
    
    return max(max(up), max(down))

# Read input
n = int(input())
nums = [int(input()) for _ in range(n)]

# Output the result
print(longest_zigzag_subsequence(nums))