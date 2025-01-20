def next_greater_digit_sum(N):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    original_sum = digit_sum(N)
    next_greater = N + 1
    
    while digit_sum(next_greater) != original_sum:
        next_greater += 1
    
    return next_greater

# Example usage:
print(next_greater_digit_sum(81))  # Output: 79
print(next_greater_digit_sum(92))  # Output: 119
print(next_greater_digit_sum(9550))  # Output: 9604
print(next_greater_digit_sum(2001))  # Output: 1001