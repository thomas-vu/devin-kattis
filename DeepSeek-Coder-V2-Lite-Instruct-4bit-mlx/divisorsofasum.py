import math

def count_divisors(n):
    sum_of_divisors = n * (n + 1) // 2
    if sum_of_divisors % 2 != 0:
        return 1
    else:
        count = 0
        sqrt_sum = int(math.sqrt(sum_of_divisors))
        for i in range(1, sqrt_sum + 1):
            if sum_of_divisors % i == 0:
                count += 1
                if i != sum_of_divisors // i:
                    count += 1
        return count

# Read input
n = int(input())
print(count_divisors(n))