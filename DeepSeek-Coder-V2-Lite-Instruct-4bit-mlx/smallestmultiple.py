from math import gcd
from functools import reduce
import sys

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm(numbers):
    lcm_result = 1
    for number in numbers:
        lcm_result = lcm(lcm_result, number)
    return lcm_result

for line in sys.stdin:
    numbers = list(map(int, line.split()))
    if not numbers:
        continue
    result = find_lcm(numbers)
    print(result)