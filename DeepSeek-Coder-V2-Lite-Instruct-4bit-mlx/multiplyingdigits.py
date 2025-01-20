def f(x, base):
    result = 1
    while x > 0:
        digit = x % base
        if digit == 0:
            return 0
        result *= digit
        x //= base
    return result

def find_smallest_x(base, number):
    low = 1
    high = min(2**64 - 1, number)
    
    while low <= high:
        mid = (low + high) // 2
        if f(mid, base) == number:
            return mid
        elif f(mid, base) < number:
            low = mid + 1
        else:
            high = mid - 1
    return "impossible"

# Read input
import sys
input_line = sys.stdin.readline().strip()
base, number = map(int, input_line.split())

# Output the result
print(find_smallest_x(base, number))