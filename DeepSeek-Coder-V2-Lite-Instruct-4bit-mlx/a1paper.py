import math

def calculate_tape(n, sheets):
    areas = [0] * (n + 1)
    for i in range(2, n + 1):
        areas[i] = areas[i - 1] / 2
    
    total_length = 0
    for i in range(2, n + 1):
        total_length += sheets[i - 2] * (2 ** (-(3 / 4) * (n - i + 1)))
    
    if total_length == 0:
        return "impossible"
    
    tape_length = total_length * (2 ** (1 / 4))
    return tape_length

# Read input
n = int(input())
sheets = list(map(int, input().split()))

# Calculate and output the result
result = calculate_tape(n, sheets)
if result == "impossible":
    print("impossible")
else:
    print("{:.10f}".format(result))