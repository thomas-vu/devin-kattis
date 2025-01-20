def is_product_divisible_by_2k(N, K, numbers):
    count_zeros = 0
    for number in numbers:
        if number % 2 == 0:
            count_zeros += 1
    
    if count_zeros >= K:
        return 1
    else:
        return 0

# Read input
N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

# Output the result
print(is_product_divisible_by_2k(N, K, numbers))