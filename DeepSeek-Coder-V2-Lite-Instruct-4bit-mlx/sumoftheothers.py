import sys

def find_sum(numbers):
    total = sum(numbers)
    for num in numbers:
        if 2 * num == total:
            return num
    return None

for line in sys.stdin:
    numbers = list(map(int, line.split()))
    sum_value = find_sum(numbers)
    print(sum_value)