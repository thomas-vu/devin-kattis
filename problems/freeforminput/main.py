import re

def sum_numbers(line):
    numbers = re.findall(r'-?\d+\.?\d*', line)
    return sum(float(num) for num in numbers)

while True:
    try:
        line = input().strip()
        if not line:
            continue
        result = sum_numbers(line)
        print("{:.6f}".format(result))
    except EOFError:
        break