import re

def is_sheldon(num):
    binary = bin(num)[2:]  # Convert number to binary string without '0b' prefix
    pattern = re.compile(r'(1{2,}0{2,}|0{2,}1{2,})')
    matches = pattern.findall(binary)
    return len(matches) > 0

def count_sheldon_numbers(x, y):
    count = 0
    for num in range(x, y + 1):
        if is_sheldon(num):
            count += 1
    return count

# Read input
x, y = map(int, input().split())

# Count and print the number of Sheldon numbers in the given range
print(count_sheldon_numbers(x, y))