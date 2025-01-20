import re

def extract_largest_number(s):
    numbers = [int(num) for num in re.findall(r'\d+', s)]
    return max(numbers)

N = int(input())
s = input()
largest_number = extract_largest_number(s)
print(largest_number)