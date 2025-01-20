def next_larger(X):
    digits = list(str(X))
    n = len(digits)
    
    # Start from the end and find the first digit that can be incremented
    for i in range(n - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            # Find the smallest digit on right side of (i+1)'th position that is greater than digits[i]
            min_index = i + 1
            for j in range(i + 2, n):
                if digits[j] > digits[i]:
                    min_index = j
            
            # Swap the found digit with digits[i]
            digits[i], digits[min_index] = digits[min_index], digits[i]
            
            # Sort the digits after the (i+1)'th position in ascending order
            result = int(''.join(digits[:i + 1] + sorted(digits[i + 1:])))
            return result if result > X else 0
    
    # If no such number found, return 0
    return 0

# Read input
X = int(input())
print(next_larger(X))