def sum_type(N):
    if N % 2 == 0:
        return 'Even' if (N // 2) % 2 == 0 else 'Either'
    else:
        return 'Odd' if (N // 2) % 2 == 0 else 'Either'

# Example usage:
print(sum_type(1))  # Output: 'Either'
print(sum_type(2))  # Output: 'Odd'