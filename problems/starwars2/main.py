def starwars_order(n, nums):
    third = n // 3
    first_third = nums[:third]
    second_third = nums[third:2*third]
    last_third = nums[2*third:]
    return second_third + first_third + last_third

n = int(input())
nums = list(map(int, input().split()))
result = starwars_order(n, nums)
print(' '.join(map(str, result)))