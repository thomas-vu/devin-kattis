def kth_number_without_0_or_8(K):
    numbers = []
    for num in range(1, 5000):
        if '0' not in str(num) and '8' not in str(num):
            numbers.append(num)
    return sorted(numbers)[K-1]

# Read input from stdin
import sys
input_line = sys.stdin.readline().strip()
K = int(input_line)

# Get the K-th number without 0 or 8
result = kth_number_without_0_or_8(K)

# Output the result
print(result)