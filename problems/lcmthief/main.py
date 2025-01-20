import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def lcm_list(numbers):
    return reduce(lambda x, y: lcm(x, y), numbers)

def find_optimal_number(numbers):
    n = len(numbers)
    min_lcm = float('inf')
    optimal_number = -1
    
    for i in range(n):
        current_numbers = numbers[:i] + numbers[i+1:]
        current_lcm = lcm_list(current_numbers)
        if current_lcm < min_lcm:
            min_lcm = current_lcm
            optimal_number = numbers[i]
        elif current_lcm == min_lcm and numbers[i] < optimal_number:
            optimal_number = numbers[i]
    
    return optimal_number

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Output the number to steal
print(find_optimal_number(numbers))