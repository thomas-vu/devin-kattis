def find_max_xor(numbers):
    max_xor = 0
    for i in range(len(numbers)):
        current_xor = 0
        for j in range(i, len(numbers)):
            current_xor ^= numbers[j]
            max_xor = max(max_xor, current_xor)
    return max_xor

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Output the result
print(find_max_xor(numbers))