import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    x = reduce(gcd, numbers)
    return x

def find_winning_number(numbers):
    min_num = min(numbers)
    max_gcd = 0
    winning_number = None
    
    for num in numbers:
        current_gcd = gcd_list([num] + [x for x in numbers if x != num])
        if current_gcd > max_gcd:
            max_gcd = current_gcd
            winning_number = num
    
    return winning_number

while True:
    try:
        line = input()
        if not line:
            continue
        numbers = list(map(int, line.split()))[1:]
        winning_number = find_winning_number(numbers)
        print(winning_number)
    except EOFError:
        break