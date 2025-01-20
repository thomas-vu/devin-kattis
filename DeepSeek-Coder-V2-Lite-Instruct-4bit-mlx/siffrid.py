def find_smallest_and_largest(N):
    digits = [int(d) for d in str(N)]
    num_digits = len(digits)
    digit_sum = sum(digits)
    
    # Find the smallest number with the same digit sum and number of digits as N
    if N == 10**(num_digits - 1):  # Special case for single-digit numbers
        smallest = N
    else:
        smallest_digits = [1] + [0] * (num_digits - 1)
        carry = 1
        for i in range(num_digits - 2, -1, -1):
            if carry:
                smallest_digits[i] += 1
                carry = 0
            if smallest_digits[i] > digits[i]:
                carry = 1
                smallest_digits[i] = 0
        if carry:
            smallest_digits.insert(0, 1)
        smallest = int(''.join(map(str, smallest_digits)))
    
    # Find the largest number with the same digit sum and number of digits as N
    largest_digits = list(digits)
    for i in range(num_digits - 1, -1, -1):
        if largest_digits[i] < 9:
            largest_digits[i] += 1
            for j in range(i + 1, num_digits):
                largest_digits[j] = min(9, digit_sum - sum(largest_digits[:i+1]))
            break
    largest = int(''.join(map(str, largest_digits)))
    
    return smallest, largest

# Input reading and output formatting
N = int(input())
smallest, largest = find_smallest_and_largest(N)
print(smallest, largest)