def find_fibonacci(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    result = []
    i = len(fib) - 1
    while n > 0:
        if fib[i] <= n:
            result.append(fib[i])
            n -= fib[i]
        i -= 1
    return result[::-1]

# Example usage:
print(*find_fibonacci(7))  # Output: 2 5
print(*find_fibonacci(12)) # Output: 3 8
print(*find_fibonacci(33)) # Output: 34 1 8