def generate_sequence(n, m, a, c, x0):
    sequence = [None] * n
    sequence[0] = (a * x0 + c) % m
    for i in range(1, n):
        sequence[i] = (a * sequence[i - 1] + c) % m
    return sequence

def count_findable_values(n, m, a, c, x0):
    sequence = generate_sequence(n, m, a, c, x0)
    findable_values = set()
    
    for value in sequence:
        if binary_search(sequence, value):
            findable_values.add(value)
    
    return len(findable_values)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

# Read input
import sys
input_line = sys.stdin.readline().strip()
n, m, a, c, x0 = map(int, input_line.split())

# Output the result
print(count_findable_values(n, m, a, c, x0))