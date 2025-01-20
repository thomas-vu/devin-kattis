def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_numbers_with_sum(A, B, S):
    count = 0
    smallest = float('inf')
    
    for number in range(A, B + 1):
        if digit_sum(number) == S:
            count += 1
            smallest = min(smallest, number)
    
    return count, smallest if count > 0 else None

# Read input
A, B, S = map(int, input().split())

# Get the result
result = find_numbers_with_sum(A, B, S)

# Output the result
if result:
    count, smallest = result
    print(count)
    if count > 0:
        print(smallest)